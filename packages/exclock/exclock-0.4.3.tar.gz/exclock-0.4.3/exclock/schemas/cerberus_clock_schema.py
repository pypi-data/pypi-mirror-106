from typing import Any, Dict, Final

from exclock.util import is_time_delta_cerberus_validate

CLOCK_SCHEMA: Final[Dict[str, Any]] = {
    'sounds':
        {
            'type': 'dict',
            'required': True,
            'keysrules': {
                'type': 'string',
                'check_with': is_time_delta_cerberus_validate,
            },
            'valuesrules':
                {
                    'type': 'dict',
                    'schema':
                        {
                            'message': {
                                'type': 'string',
                                'required': True,
                            },
                            'sound_filename': {
                                'type': 'string',
                            },
                        },
                }
        },
    'loop': {
        'type': 'integer',
        'nullable': True,
        },
    'show_message': {
        'type': 'boolean',
        },
    'title': {
        'type': 'string',
        }
}
