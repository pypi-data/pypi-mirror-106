"""SPICE toolbox module."""

from .fov import SpiceFieldOfView
from .pool import SPICEPool, SpicePool, debug_spice_pool
from .references import (
    SpiceBody, SpiceInstrument, SpiceObserver,
    SPICERef, SpiceRef, SpiceSpacecraft
)
from .times import et, et_ca_range, et_range, et_ranges, tdb, utc


__all__ = [
    'et',
    'et_range',
    'et_ranges',
    'et_ca_range',
    'tdb',
    'utc',
    'SpiceBody',
    'SpiceFieldOfView',
    'SpiceObserver',
    'SpiceInstrument',
    'SpicePool',
    'SpiceRef',
    'SpiceSpacecraft',
    'debug_spice_pool',
    'SPICERef',   # Depreciated
    'SPICEPool',  # Depreciated
]
