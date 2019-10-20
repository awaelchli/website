from wagtail.admin.rich_text.converters.html_to_contentstate import InlineStyleElementHandler
from wagtail.admin.rich_text.editors.draftail.features import InlineStyleFeature
from wagtail.core import hooks


@hooks.register('register_rich_text_features')
def register_code_styling(features):
    feature_name = 'code'
    type_ = 'CODE'
    tag = 'code'

    control = {
        'type': type_,
        'icon': 'fa-code',
        'description': 'Code'
    }

    features.register_editor_plugin(
        'draftail',
        feature_name,
        InlineStyleFeature(control)
    )

    db_conversion = {
        'from_database_format': {
            tag: InlineStyleElementHandler(type_)
        },
        'to_database_format': {
            'style_map': {
                type_: {
                    'element': tag
                }
            }
        },
    }

    features.register_converter_rule('contentstate', feature_name, db_conversion)

    # Will register this feature with all richtext editors by default
    features.default_features.append(feature_name)
