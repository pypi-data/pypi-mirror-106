"""Trajectory module."""  # pylint: disable=too-many-lines

import numpy as np

from matplotlib.collections import PathCollection
from matplotlib.path import Path

from .mask_traj import MaskedTrajectory
from ..math.vectors import angle, ell_norm, norm
from ..misc import cached_property, logger
from ..spice import (
    SpiceBody, SpiceInstrument, SpicePool, SpiceRef,
    SpiceSpacecraft, et, et_ca_range, et_range, utc
)
from ..spice.toolbox import (
    attitude, boresight_pt, fov_pts, groundtrack_velocity,
    illum_angles, local_time, radec, rlonlat, sc_state,
    solar_longitude, sub_obs_pt, sun_pos, true_anomaly
)


log_traj, debug_trajectory = logger('Trajectory')


class Trajectory:  # pylint: disable=too-many-public-methods
    """Spacecraft trajectory object.

    Parameters
    ----------
    kernels: str or tuple
        List of kernels to be loaded in the SPICE pool.

    observer: str or spice.SpiceSpacecraft or spice.SpiceInstrument
        Observer (spacecraft or instrument) SPICE reference.

    target: str or spice.SpiceBody
        Target SPICE reference.

    ets: float or str or list
        Ephemeris time(s).

    abcorr: str, optional
        Aberration corrections to be applied when computing
        the target's position and orientation.
        Only the SPICE keys are accepted.

    Raises
    ------
    ValueError
        If the provided observer is not a valid spacecraft or instrument.

    """

    TOO_MANY_POINTS_WARNING = 1_000_000

    def __init__(self, kernels, observer, target, ets, abcorr='NONE'):
        self.kernels = kernels

        # Init SPICE references
        self.target = SpiceBody(target)
        self.observer = observer

        # Init ephemeris times
        self.ets = ets

        # Optional parameters
        self.abcorr = abcorr

    def __repr__(self):
        return (
            f'<{self.__class__.__name__}> '
            f'Observer: {self.observer} | '
            f'Target: {self.target}'
            f'\n - UTC start time: {self.start}'
            f'\n - UTC stop time: {self.stop}'
            f'\n - Nb of pts: {len(self):,d}'
        )

    def __len__(self):
        return len(self.ets)

    def __and__(self, other):
        """And ``&`` operator."""
        return self.mask(self.intersect(other))

    def __xor__(self, other):
        """Hat ``^`` operator."""
        return self.mask(self.intersect(other, outside=True))

    def __getitem__(self, item):
        if item.upper() in ['SUN', 'SS']:
            return self.ss

        try:
            # pylint: disable=no-member
            observer = self.observer.instr(item) \
                if isinstance(self, SpacecraftTrajectory) else \
                SpiceRef(item)

            return Trajectory(
                self.kernels,
                observer,
                self.target,
                self.ets,
                abcorr='NONE')

        except ValueError:
            pass

        try:
            return Trajectory(
                self.kernels,
                self.observer,
                SpiceBody(item),
                self.ets,
                abcorr='NONE')
        except KeyError:
            pass

        raise KeyError(
            'The item must be a spacecraft, an instrument, a target body or the SUN. ')

    @property
    def kernels(self):
        """Get the list of kernels to used."""
        return self.__kernels

    @kernels.setter
    def kernels(self, kernels):
        """List of kernels setter.

        Note
        ----
        SPICE pool content is checked to see if
        all the kernels are correctly loaded.
        If it's not the case, the pool will
        be purge and refilled.

        """
        self.__kernels = kernels

        if SpicePool != kernels:
            log_traj.info('Load the kernels to the pool.')
            SpicePool.add(kernels, purge=True)

    @property
    def observer(self):
        """Get observer."""
        return self.__observer

    @observer.setter
    def observer(self, observer):
        self.__observer = SpiceRef(observer)

        if isinstance(self.observer, SpiceSpacecraft):
            self.__class__ = SpacecraftTrajectory

        elif isinstance(self.observer, SpiceInstrument):
            self.__class__ = InstrumentTrajectory

        else:
            raise ValueError(f'The observer `{self.observer}` must be a'
                             '`spacecraft` or an `instrument` reference.')

    @property
    def spacecraft(self):
        """Observer spacecraft SPICe reference."""
        return self.observer.spacecraft

    @property
    def ets(self):
        """Ephemeris times."""
        return self.__ets

    @ets.setter
    def ets(self, ets):
        """Ephemeris times setter."""
        log_traj.debug('Init ephemeris time.')

        if isinstance(ets, str):
            self.__ets = np.array([et(ets)])
        elif isinstance(ets, (int, float)):
            self.__ets = np.array([ets])
        elif isinstance(ets, slice):
            self.__ets = et_range(ets.start, ets.stop, ets.step)
        elif isinstance(ets, (tuple, list, np.ndarray)):
            self.__ets = np.array(sorted([
                et(t) if isinstance(t, str) else t for t in ets]))
        else:
            raise ValueError('Invalid input Ephemeris Time(s).')

        if len(self.__ets) > self.TOO_MANY_POINTS_WARNING:
            log_traj.warning(
                'You have selected more than %s points. '
                'SPICE computation can take a while. '
                'It may be relevant to reduce the temporal '
                'resolution or the time range.',
                f'{self.TOO_MANY_POINTS_WARNING:,d}')

    @cached_property
    def utc(self):
        """UTC times."""
        log_traj.info('Compute UTC times.')
        return utc(self.ets)

    @property
    def start(self):
        """UTC start time."""
        return utc(self.ets[0])

    @property
    def stop(self):
        """UTC stop time."""
        return utc(self.ets[-1])

    @property
    def abcorr(self):
        """SPICE aberration correction."""
        return self.__abcorr

    @abcorr.setter
    def abcorr(self, key):
        """SPICE aberration correction setter."""
        if key.replace(' ', '').upper() not in [
            'NONE', 'LT', 'LT+S', 'CN', 'CN+S',
            'XLT', 'XLT+S', 'XCN', 'XCN+S',
        ]:
            raise KeyError(f'Invalid aberration correction key:`{key}`')
        self.__abcorr = key.upper()

    @property
    def boresight(self):
        """Observer boresight pointing vector."""
        return self.observer.boresight

    @boresight.setter
    def boresight(self, boresight):
        """Observer boresight setter."""
        if isinstance(self.observer, SpiceInstrument):
            raise AttributeError('SpiceInstrument boresight can not be changed')

        log_traj.info('Change boresight from %r to %r.',
                      self.boresight, boresight)

        # Invalided cached values that require the previous boresight
        del self.boresight_pts
        del self.radec

        # Change observer boresight
        self.observer.BORESIGHT = boresight

    @property
    def inertial_frame(self):
        """Target parent inertial frame."""
        return 'JUICE_JUPITER_IF_J2000' if self.spacecraft == 'JUICE' and \
            (self.target == 'JUPITER' or self.target.parent == 'JUPITER') else \
            'ECLIPJ2000'

    @cached_property
    def sc_pts(self):
        """Sub-spacecraft surface intersection vector.

        Returns
        -------
        np.ndarray
            Spacecraft XYZ intersection on the target body fixed frame
            (expressed in km).

        Note
        ----
        Currently the intersection method is fixed internally
        as ``method='NEAR POINT/ELLIPSOID'``.

        See Also
        --------
        Trajectory.lonlat
        Trajectory.rlonlat
        Trajectory.lon_e
        Trajectory.lat
        Trajectory.local_time
        Trajectory.illum_angles
        Trajectory.solar_zenith_angle

        """
        log_traj.info('Compute sub-spacecraft points.')
        res = sub_obs_pt(
            self.ets,
            self.spacecraft,
            self.target,
            abcorr=self.abcorr,
            method='NEAR POINT/ELLIPSOID')

        log_traj.debug('Result: %r', res)
        return res

    @cached_property(parent='sc_pts')
    def sc_rlonlat(self):
        """Sub-spacecraft coordinates.

        Returns
        -------
        np.ndarray
            Sub-spacecraft planetocentric coordinates:
            radii, east longitudes and latitudes.

        Note
        ----
        Currently the intersection method is fixed internally
        as ``method='NEAR POINT/ELLIPSOID'``.

        See Also
        --------
        Trajectory.sc_pts
        Trajectory.lon_e
        Trajectory.lat

        """
        log_traj.debug('Compute sub-observer point in planetocentric coordinates.')
        return rlonlat(self.sc_pts)

    @property
    def lonlat(self):
        """Groundtrack or surface intersect (not implemented here)."""

    @cached_property
    def boresight_pts(self):
        """Boresight surface intersection vector.

        Returns
        -------
        np.ndarray
            Boresight XYZ intersection on the target body fixed frame
            (expressed in km).

        Note
        ----
        Currently the intersection method is fixed internally
        as ``method='ELLIPSOID'``.

        """
        log_traj.info('Compute boresight intersection points.')
        res = boresight_pt(
            self.ets,
            self.observer,
            self.target,
            abcorr=self.abcorr,
            method='ELLIPSOID')

        log_traj.debug('Result: %r', res)
        return res

    @cached_property(parent='boresight_pts')
    def boresight_rlonlat(self):
        """Boresight surface intersect coordinates.

        Returns
        -------
        np.ndarray
            Boresight surface intersect planetocentric coordinates:
            radii, east longitudes and latitudes.

        See Also
        --------
        Trajectory.boresight_pts

        """
        log_traj.debug('Compute boresight intersect in planetocentric coordinates.')
        return rlonlat(self.boresight_pts)

    @property
    def surface(self):
        """Boresight intersection on the target surface."""
        return ~np.isnan(self.boresight_pts[0])

    @property
    def limb(self):
        """Limb viewing geometry.

        Masked then boresight intersection the target surface.

        """
        return ~self.surface

    @cached_property(parent='sc_pts')
    def sc_illum_angles(self):
        """Sub-spacecraft illumination angles (degree).

        Incidence, emission and phase angles.

        See Also
        --------
        Trajectory.inc
        Trajectory.emi
        Trajectory.phase
        Trajectory.sc_pts

        """
        log_traj.info('Compute sub-spacecraft illumination geometry.')
        return illum_angles(
            self.ets,
            self.observer,
            self.target,
            self.sc_pts,
            abcorr=self.abcorr,
            method='ELLIPSOID',
        )

    @cached_property(parent='boresight_pts')
    def boresight_illum_angles(self):
        """Instrument surface intersec illumination angles (degree).

        Incidence, emission and phase angles.

        See Also
        --------
        Trajectory.inc
        Trajectory.emi
        Trajectory.phase
        Trajectory.boresight_pts

        """
        log_traj.info('Compute boresight intersection illumination geometry.')
        return illum_angles(
            self.ets,
            self.observer,
            self.target,
            self.boresight_pts,
            abcorr=self.abcorr,
            method='ELLIPSOID',
        )

    @cached_property
    def sc_state(self):
        """Spacecraft position and velocity in the target body fixed frame (km and km/s).

        See Also
        --------
        Trajectory.sc_pos
        Trajectory.alt

        """
        log_traj.info('Compute spacecraft position and velocity in the target frame.')
        res = sc_state(
            self.ets,
            self.spacecraft,
            self.target,
            abcorr=self.abcorr)

        log_traj.debug('Result: %r', res)
        return res

    @property
    def sc_pos(self):
        """Spacecraft position in the target body fixed frame (km).

        See Also
        --------
        Trajectory.dist
        Trajectory.alt

        """
        return self.sc_state[:3]

    @property
    def sc_velocity(self):
        """Spacecraft velocity vector in the target body fixed frame (km/s).

        See Also
        --------
        Trajectory.sc_speed

        """
        return self.sc_state[3:]

    @cached_property(parent='sc_state')
    def sc_speed(self):
        """Observer speed in the target body fixed frame (km/s).

        See Also
        --------
        Trajectory.sc_velocity

        """
        return norm(self.sc_velocity.T)

    @cached_property(parent='sc_state')
    def dist(self):
        """Spacecraft distance to the body target center (km).

        This distance is computed to the center of the targeted body.

        See Also
        --------
        Trajectory.sc_pos
        Trajectory.alt
        Trajectory.slant

        """
        log_traj.debug('Compute spacecraft distance in the target frame.')
        return norm(self.sc_pos.T)

    @cached_property(parent=('sc_pts', 'sc_state'))
    def alt(self):
        """Spacecraft altitude to the sub-spacecraft point (km).

        The intersect on the surface is computed on the reference
        ellipsoide.

        See Also
        --------
        Trajectory.sc_pts
        Trajectory.sc_pos
        Trajectory.dist

        """
        log_traj.debug('Compute spacecraft distance in the target frame.')
        return norm(self.sc_pos.T - self.sc_pts.T)

    @cached_property(parent='sc_state')
    def groundtrack_velocity(self):
        """Compute the groundtrack velocity (km/s).

        It correspond to the motion speed of the sub-spacecraft point
        on the surface.

        See Also
        --------
        Trajectory.sc_state
        Trajectory.sc_pos
        Trajectory.sc_velocity

        """
        log_traj.info('Compute groundtrack velocity.')
        res = groundtrack_velocity(self.target, self.sc_state)

        log_traj.debug('Result: %r', res)
        return res

    @cached_property
    def sc_attitude(self):
        """Spacecraft attitude c-matrix in J2000 frame."""
        log_traj.info('Compute spacecraft attitude.')
        return attitude(self.ets, self.observer)

    @cached_property(parent='sc_attitude')
    def radec(self):
        """Boresight RA/DEC pointing in J2000 frame."""
        log_traj.info('Compute spacecraft pointing (RA/DEC).')
        return radec(np.einsum('ijk,j->ik',
                               self.sc_attitude,
                               self.boresight,
                               optimize=True))

    @property
    def ra(self):
        """Boresight pointing right ascension angle (degree)."""
        return self.radec[0]

    @property
    def dec(self):
        """Boresight pointing declination angle (degree)."""
        return self.radec[1]

    @cached_property
    def sun_pos(self):
        """Sun position in the target body fixed frame (km).

        Note
        ----
        Currently the intersection method is fixed on a sphere
        and the input time at the target center is not corrected
        from light travel.

        See Also
        --------
        Trajectory.sun_rlonlat
        Trajectory.sun_lon_e
        Trajectory.sun_lat
        Trajectory.sun_lonlat
        Trajectory.solar_zenith_angle

        """
        log_traj.info('Compute Sun coordinates in the target frame.')
        res = sun_pos(
            self.ets,
            self.target,
            abcorr=self.abcorr)

        log_traj.debug('Result: %r', res)
        return res

    @cached_property(parent='sun_pos')
    def sun_rlonlat(self):
        """Sub-solar coordinates.

        Returns
        -------
        np.ndarray
            Sub-solar planetocentric coordinates:
            radii, east longitudes and longitudes.

        See Also
        --------
        Trajectory.sun_pos
        Trajectory.sun_lon_e
        Trajectory.sun_lat
        Trajectory.sun_lonlat

        """
        log_traj.debug('Compute sub-solar point in planetocentric coordinates.')
        return rlonlat(self.sun_pos)

    @property
    def sun_lon_e(self):
        """Sub-solar point east longitude (degree)."""
        return self.sun_rlonlat[1]

    @property
    def sun_lat(self):
        """Sub-solar point latitude (degree)."""
        return self.sun_rlonlat[2]

    @property
    def sun_lonlat(self):
        """Sub-solar point groundtrack (degree)."""
        return self.sun_rlonlat[1:]

    @property
    def ss(self):
        """Alias on the sub-solar point groundtrack (degree)."""
        return self.sun_lonlat

    @cached_property
    def solar_longitude(self):
        """Target seasonal solar longitude (degrees).

        Warning
        -------
        The seasonal solar longitude is computed on the main parent body
        for the moons (`spiceypy.lspcn` on the moon will not return
        the correct expected value).

        """
        log_traj.info('Compute the target seasonal solar longitude.')
        res = solar_longitude(
            self.ets,
            self.target,
            abcorr=self.abcorr)

        log_traj.debug('Result: %r', res)
        return res

    @cached_property
    def true_anomaly(self):
        """Target orbital true anomaly (degree)."""
        log_traj.debug('Compute true anomaly angle.')

        res = true_anomaly(
            self.ets,
            self.target,
            abcorr=self.abcorr,
            frame=self.inertial_frame)

        log_traj.debug('Result: %r', res)
        return res

    def mask(self, cond):
        """Create a masked trajectory."""
        return MaskedTrajectory(self, cond)

    def where(self, cond):
        """Create a masked trajectory only where the condition is valid."""
        return self.mask(~cond)

    def intersect(self, obj, outside=False):
        """Intersection mask between the trajectory and an object.

        Parameters
        ----------
        obj: any
            ROI-like object to intersect the trajectory.
        outside: bool, optional
            Return the invert of the intersection (default: `False`).

        Returns
        -------
        MaskedTrajectory
            Mask to apply on the trajectory.

        Raises
        ------
        AttributeError
            If the comparison object doest have a :py:func:`constains`
            test function.

        """
        if not hasattr(obj, 'contains'):
            raise AttributeError(f'Undefined `contains` intersection in {obj}.')

        cond = obj.contains(self.lonlat)
        return cond if outside else ~cond

    @property
    def approx_ca_utc(self):
        """List of approximate closest approach UTC times to the target.

        Danger
        ------
        These values may not be accurate depending on the
        :py:class:`Trajectory` temporal resolution.

        """
        return [
            self.utc[seg][np.argmin(self.dist[seg])]
            # pylint: disable=comparison-with-callable
            for seg in self.where(self.dist <= Flyby.DIST_MIN).seg
        ]

    @property
    def flybys(self):
        """Get all the flybys for this trajectory."""
        return [
            Flyby(self.kernels, self.observer, self.target, ca_utc, abcorr=self.abcorr)
            for ca_utc in self.approx_ca_utc
        ]


class SpacecraftTrajectory(Trajectory):
    """Spacecraft trajectory object."""

    @property
    def lon_e(self):
        """Sub-spacecraft east longitude (degree)."""
        return self.sc_rlonlat[1]

    @property
    def lat(self):
        """Sub-spacecraft latitude (degree)."""
        return self.sc_rlonlat[2]

    @property
    def lonlat(self):
        """Sub-spacecraft groundtrack east longitudes and latitudes (degree)."""
        return self.sc_rlonlat[1:]

    @cached_property(parent='sc_rlonlat')
    def local_time(self):
        """Sub-spacecraft local time (decimal hours).

        See Also
        --------
        Trajectory.rlonlat

        """
        log_traj.info('Compute sub-spacecraft local time.')
        return local_time(self.ets, self.lon_e, self.target)

    @property
    def slant(self):
        """Spacecraft line-of-sight distance to the sub-spacecraft point (km).

        This is not the distance the distance to the target body center,
        but an alias of the altitude of the spacecraft.

        See Also
        --------
        Trajectory.dist
        Trajectory.alt

        """
        return self.alt

    @property
    def inc(self):
        """Sub-spacecraft incidence angle (degree)."""
        return self.sc_illum_angles[0]

    @property
    def emi(self):
        """Sub-spacecraft emission angle (degree)."""
        return self.sc_illum_angles[1]

    @property
    def phase(self):
        """Sub-spacecraft phase angle (degree)."""
        return self.sc_illum_angles[2]

    @cached_property(parent='sc_illum_angles')
    def day(self):
        """Day side, sub-spacecraft incidence lower than 90°."""
        return self.inc <= 90

    @cached_property(parent='sc_illum_angles')
    def night(self):
        """Night side, sub-spacecraft incidence larger than 90°."""
        return self.inc > 90

    @cached_property(parent='sc_illum_angles')
    def nadir(self):
        """Nadir viewing, always True for the sub-spacecraft point."""
        return np.full_like(self.ets, True, dtype=bool)

    @cached_property(parent='sc_illum_angles')
    def off_nadir(self):
        """Off-nadir viewing, always False for the sub-spacecraft point."""
        return np.full_like(self.ets, False, dtype=bool)

    @cached_property(parent='sc_pts')
    def ell_norm(self):
        """Sub-spacecraft local normal.

        Unitary vector pointing upward from the surface of the ellipsoid.

        See Also
        --------
        Trajectory.sc_pts

        """
        log_traj.debug('Compute sub-observer local normal.')
        res = ell_norm(self.sc_pts.T, self.target.radii).T

        log_traj.debug('Result: %r', res)
        return res

    @cached_property(parent=('sc_pts', 'sun_pos', 'ell_norm'))
    def solar_zenith_angle(self):
        """Sub-spacecraft solar zenith angle (degree).

        The angle is computed from the local normal
        on the ellipsoid. If the targeted body is a sphere,
        this value much be equal to the incidence angle.

        See Also
        --------
        Trajectory.sun_pos
        Trajectory.sc_pts
        Trajectory.ell_norm

        """
        log_traj.debug('Compute sub-observer solar zenith angle.')
        res = angle(self.sun_pos.T - self.sc_pts.T,
                    self.ell_norm.T)  # pylint: disable=no-member

        log_traj.debug('Result: %r', res)
        return res


class InstrumentTrajectory(Trajectory):
    """Instrument trajectory object."""
    FOV_PTS = 25

    @property
    def lon_e(self):
        """Instrument surface intersect east longitude (degree)."""
        return self.boresight_rlonlat[1]

    @property
    def lat(self):
        """Instrument surface intersect latitude (degree)."""
        return self.boresight_rlonlat[2]

    @property
    def lonlat(self):
        """Instrument surface intersect east longitudes and latitudes (degree)."""
        return self.boresight_rlonlat[1:]

    @cached_property(parent='boresight_rlonlat')
    def local_time(self):
        """Instrument surface intersec local time (decimal hours)."""
        log_traj.info('Compute boresight intersection local time.')
        return local_time(self.ets, self.lon_e, self.target)

    @cached_property(parent=('sc_pts', 'boresight_pts'))
    def slant(self):
        """Line-of-sight distance to the boresight surface intersection (km)."""
        log_traj.debug('Compute slant range to the boresight surface intersection.')
        return norm(self.sc_pos.T - self.boresight_pts.T)

    @property
    def inc(self):
        """Instrument surface intersec incidence angle (degree)."""
        return self.boresight_illum_angles[0]

    @property
    def emi(self):
        """Instrument surface intersec emission angle (degree)."""
        return self.boresight_illum_angles[1]

    @property
    def phase(self):
        """Instrument surface intersec phase angle (degree)."""
        return self.boresight_illum_angles[2]

    @cached_property(parent='boresight_illum_angles')
    def day(self):
        """Day side, boresight intersection incidence lower than 90°."""
        return self.inc <= 90

    @cached_property(parent='boresight_illum_angles')
    def night(self):
        """Night side, boresight intersection incidence larger than 90°."""
        return self.inc > 90

    @cached_property(parent='boresight_illum_angles')
    def nadir(self):
        """Nadir viewing, boresight intersection emission angle is lower than 1°."""
        return self.emi < 1

    @cached_property(parent='boresight_illum_angles')
    def off_nadir(self):
        """Off-nadir viewing, boresight intersection emission angle is larger than 1°."""
        return self.emi >= 1

    @cached_property(parent='boresight_pts')
    def ell_norm(self):
        """Instrument surface intersec local normal.

        Unitary vector pointing upward from the surface of the ellipsoid.

        See Also
        --------
        Trajectory.boresight_pts

        """
        log_traj.debug('Compute sub-observer local normal.')
        res = ell_norm(self.boresight_pts.T, self.target.radii).T

        log_traj.debug('Result: %r', res)
        return res

    @cached_property(parent=('boresight_pts', 'sun_pos', 'ell_norm'))
    def solar_zenith_angle(self):
        """Instrument surface intersec solar zenith angle (degree).

        The angle is computed from the local normal
        on the ellipsoid. If the targeted body is a sphere,
        this value much be equal to the incidence angle.

        See Also
        --------
        Trajectory.sun_pos
        Trajectory.boresight_pts
        Trajectory.ell_norm

        """
        log_traj.debug('Compute sub-observer solar zenith angle.')
        res = angle(self.sun_pos.T - self.boresight_pts.T,
                    self.ell_norm.T)  # pylint: disable=no-member

        log_traj.debug('Result: %r', res)
        return res

    @cached_property
    def fov_pts(self):
        """Instrument FOV points.

        Note
        ----
        Currently the intersection method is fixed internally
        as ``method='ELLIPSOID'``.

        """
        log_traj.debug('Compute FOV intersection points.')
        res = fov_pts(
            self.ets,
            self.observer,
            self.target,
            limb=True,
            npt=self.FOV_PTS - 1,
            abcorr=self.abcorr,
            method='ELLIPSOID')

        # Close the polygon
        res = np.dstack([res, res[..., 0]])

        log_traj.debug('Result: %r', res)
        return res

    @cached_property(parent='fov_pts')
    def fov_rlonlat(self):
        """Instrument FOV intersect coordinates.

        Returns
        -------
        np.ndarray
            Boresight surface intersect planetocentric coordinates:
            radii, east longitudes and latitudes.

        See Also
        --------
        Trajectory.fov_pts

        """
        log_traj.debug('Compute FOV intersects planetocentric coordinates.')
        return rlonlat(self.fov_pts)

    @cached_property(parent='fov_rlonlat')
    def fov_paths(self):
        """Instrument FOV surface paths.

        Note
        ----
        If all the points are above the limb the path is set to ``None``.

        See Also
        --------
        Trajectory.fov_rlonlat

        """
        log_traj.debug('Compute FOV paths.')
        r_max = max(self.target.radii)

        return [
            Path(rlonlat[..., 1:]) if np.min(rlonlat[..., 0]) < r_max else None
            for rlonlat in np.moveaxis(self.fov_rlonlat, 0, -1)
        ]

    def fovs(self, label=None, **kwargs):
        """Instrument field of view paths collection."""
        label = str(self.observer).replace('_', ' ') if label is None else label
        return PathCollection(self.fov_paths, label=label, **kwargs)


class Flyby(Trajectory):
    """Trajectory flyby object.

    The location of the closest approach point is
    recomputed internally to ensure that the flyby is correctly
    center on its lowest altitude with a resolution of 1 sec.

    To ensure better performances, the CA location is found
    in a 3 steps process:

    - 1st stage with a coarse resolution (20 min at CA ± 12h)
    - 2nd stage with a medium resolution (1 min at CA ± 30 min)
    - 3rd stage with a fine resolution (1 sec at CA ± 2 min)

    By default the final sampling temporal steps are irregular
    with a high resolution only around the CA:

    - 1 pt from CA -12 h to CA  -2 h every 10 min
    - 1 pt from CA  -2 h to CA  -1 h every  1 min
    - 1 pt from CA  -1 h to CA -10 m every 10 sec
    - 1 pt from CA -10 m to CA +10 m every  1 sec
    - 1 pt from CA +10 m to CA  +1 h every 10 sec
    - 1 pt from CA  +1 h to CA  +2 h every  1 min
    - 1 pt from CA  +2 h to CA +12 h every 10 min

    = ``2,041 points`` around the CA point.

    Parameters
    ----------
    kernels: str or tuple
        List of kernels to be loaded in the SPICE pool.

    observer: str or spice.SpiceSpacecraft
        Observer SPICE reference.

    target: str or spice.SpiceBody
        Target SPICE reference.

    approx_ca_utc: float, string or numpy.datetime64
        Approximate CA datetime. This value will be re-computed.

    *dt: tuple(s), optional
        Temporal sequence around closest approach:

        `(duration, numpy.datetime unit, step value and unit)`

        See :py:func:`moon_coverage.spice.et_ca_range` for more details.

    abcorr: str, optional
        Aberration corrections to be applied when computing
        the target's position and orientation.
        Only the SPICE keys are accepted.

    See Also
    --------
    Trajectory
    moon_coverage.spice.et_ca_range

    Raises
    ------
    AltitudeTooHighError
        If the target altitude is too high (above ``100,000 km``)

    """

    DIST_MIN = 100_000  # Distance minimal to a given target [km]

    def __init__(self, kernels, observer, target, approx_ca_utc, *dt, abcorr='NONE'):
        # Check the pool coverage
        et_min, et_max = SpicePool.coverage(observer, target, fmt='ET')

        # Coarse stage
        coarse_ets = et_ca_range(approx_ca_utc, (24, 'h', '20 min'))
        coarse_ets = coarse_ets[(et_min <= coarse_ets) & (coarse_ets <= et_max)]

        log_traj.info('Coarse UTC window: %s', utc(coarse_ets[0], coarse_ets[-1]))

        coarse_traj = Trajectory(kernels, observer, target, coarse_ets)
        coarse_ca_utc = coarse_traj.utc[np.argmin(coarse_traj.dist)]

        log_traj.info('Coarse CA UTC: %s', coarse_ca_utc)

        # Medium stage
        medium_ets = et_ca_range(coarse_ca_utc, (30, 'm', '1 min'))
        medium_ets = medium_ets[(et_min <= medium_ets) & (medium_ets <= et_max)]

        log_traj.info('Medium UTC window: %s', utc(medium_ets[0], medium_ets[-1]))

        medium_traj = Trajectory(kernels, observer, target, medium_ets)
        medium_ca_utc = medium_traj.utc[np.argmin(medium_traj.dist)]

        log_traj.info('Medium CA UTC: %s', medium_ca_utc)

        # Fine stage
        fine_ets = et_ca_range(medium_ca_utc, (2, 'm', '1 sec'))
        fine_ets = fine_ets[(et_min <= fine_ets) & (fine_ets <= et_max)]

        log_traj.info('Fine UTC window: %s', utc(fine_ets[0], fine_ets[-1]))

        fine_traj = Trajectory(kernels, observer, target, fine_ets)
        fine_ca_utc = fine_traj.utc[np.argmin(fine_traj.alt)]

        # Round [ms] digits to 1 sec precision
        fine_ca_utc = (fine_ca_utc + np.timedelta64(500, 'ms')).astype('datetime64[s]')

        log_traj.info('Fine CA UTC: %s', fine_ca_utc)

        # Check min altitude to make sure its valid flyby
        fine_ca_alt = fine_traj.alt[np.argmin(fine_traj.alt)]

        if fine_ca_alt > self.DIST_MIN:
            raise AltitudeTooHighError(
                f'{fine_ca_alt:,.1f} km > {self.DIST_MIN:,.1f} km at CA')

        # Select the flyby temporal grid
        ets = et_ca_range(fine_ca_utc, *dt)
        ets = ets[(et_min <= ets) & (ets <= et_max)]

        super().__init__(kernels, observer, target, ets)

        if isinstance(self, SpacecraftTrajectory):
            self.__class__ = SpacecraftFlyby
        else:
            self.__class__ = InstrumentFlyby

    def __repr__(self):
        return (
            f'<{self.__class__.__name__}> '
            f'Observer: {self.observer} | '
            f'Target: {self.target}'
            f'\n - Altitude at CA: {self.alt_ca:,.1f} km'
            f'\n - UTC at CA: {self.utc_ca}'
            f'\n - Duration: {self.duration}'
            f'\n - Nb of pts: {len(self):,d}'
        )

    def __getitem__(self, item):
        traj = super().__getitem__(item)

        if isinstance(traj, SpacecraftTrajectory):
            traj.__class__ = SpacecraftFlyby

        elif isinstance(traj, InstrumentTrajectory):
            traj.__class__ = InstrumentFlyby

        return traj

    @property
    def duration(self):
        """Flyby duration."""
        return (self.stop - self.start).item()

    @cached_property
    def _i_ca(self):
        """Closest approach index."""
        return np.argmin(self.alt)

    @property
    def et_ca(self):
        """Closest approach ET time."""
        return self.ets[self._i_ca]

    @property
    def utc_ca(self):
        """Closest approach UTC time."""
        return self.utc[self._i_ca].astype('datetime64[s]')

    @property
    def date_ca(self):
        """Closest approach date."""
        return np.datetime64(self.utc_ca, 'D')

    @property
    def t_ca(self):
        """Time to closest approach."""
        return (self.utc - self.utc_ca).astype('timedelta64[s]')

    @property
    def lon_e_ca(self):
        """Sub-spacecraft west longitude at closest approach."""
        return self.lonlat[0][self._i_ca]

    @property
    def lat_ca(self):
        """Sub-spacecraft latitude at closest approach."""
        return self.lonlat[1][self._i_ca]

    @property
    def alt_ca(self):
        """Altitude at closest approach (km)."""
        return self.alt[self._i_ca]

    @cached_property
    def ca(self):
        """Closest approach point."""
        return Trajectory(self.kernels, self.observer, self.target, self.et_ca)

    @staticmethod
    def _interp(alt, alts, ets):
        """Interpolate UTC time for a given altitude."""
        if len(ets) > 1:
            if alt < alts.min():
                raise AltitudeTooLowError(f'{alt:,.1f} km < {alts.min():,.1f} km at CA')

            if alt > alts.max():
                raise AltitudeTooHighError(f'{alt:,.1f} km > {alts.max():,.1f} km at CA')

            if np.sum(alts[1:] >= alts[:-1]) != len(alts) - 1:
                raise ValueError('The function is not strictly increasing.')

            et_alt = np.interp(alt, alts, ets)
        else:
            et_alt = ets[0]

        return utc(et_alt, unit='s')

    @property
    def inbound(self):
        """Inbound part of the flyby, before CA."""
        return slice(self._i_ca, None, -1)

    @property
    def outbound(self):
        """Outbound part of the flyby, after CA."""
        return slice(self._i_ca, None)

    def alt_window(self, alt):
        """Interpolated altitude window during the flyby.

        Parameters
        ----------
        alt: float
            Altitude reach to start and stop the window (in km).

        Return
        ------
        numpy.datetime64, numpy.datetime64, numpy.timedelta64
            UTC start, stop times and duration.

        Raises
        ------
        AltitudeTooLowError
            If the altitude provided is lower than the CA altitude.
        AltitudeTooHighError
            If the altitude provided is higher than the
            max altitude of the flyby.

        """
        start = self._interp(alt, self.alt[self.inbound], self.ets[self.inbound])
        stop = self._interp(alt, self.alt[self.outbound], self.ets[self.outbound])

        return start, stop, (stop - start).item()


class SpacecraftFlyby(Flyby, SpacecraftTrajectory):
    """Spacecraft flyby object."""


class InstrumentFlyby(Flyby, InstrumentTrajectory):
    """Instrument flyby object."""


class AltitudeTooLowError(Exception):
    """Min value is too low and never reach during the flyby."""


class AltitudeTooHighError(Exception):
    """Min value is too high and not sampled during the flyby."""
