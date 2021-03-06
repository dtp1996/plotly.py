import _plotly_utils.basevalidators


class PositionValidator(_plotly_utils.basevalidators.NumberValidator):

    def __init__(
        self, plotly_name='position', parent_name='layout.yaxis', **kwargs
    ):
        super(PositionValidator, self).__init__(
            plotly_name=plotly_name,
            parent_name=parent_name,
            edit_type='plot+margins',
            max=1,
            min=0,
            role='style',
            **kwargs
        )
