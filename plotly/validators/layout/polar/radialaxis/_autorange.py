import _plotly_utils.basevalidators


class AutorangeValidator(_plotly_utils.basevalidators.EnumeratedValidator):

    def __init__(
        self,
        plotly_name='autorange',
        parent_name='layout.polar.radialaxis',
        **kwargs
    ):
        super(AutorangeValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='calc',
            implied_edits={},
            role='style',
            values=[True, False, 'reversed'],
            **kwargs
        )
