import matplotlib.pyplot as plt
from io import BytesIO


class Visualizer:
    def __init__(self, model_name, base_url):
        self.model_name = model_name
        self.base_url = base_url

    def execute(self, analysis, df):
        fig, ax = plt.subplots()
        df.plot(ax=ax)
        buffer = BytesIO()
        plt.savefig(buffer, format="png")
        buffer.seek(0)
        return buffer.getvalue()
