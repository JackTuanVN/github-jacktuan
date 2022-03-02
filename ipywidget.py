''''import ipywidgets as widgets

ignition = widgets.ToggleButton(
    value=False,
    description='Start Engine',
    button_style='success',
    tooltip='Engage your Engine',
    icon='rocket'
)

output = widgets.Output()

display(ignition, output)

def on_value_change(change):
    with output:
        if change['new'] == True:
            print("engine started!")
        else:   
            print("engine stopped")

ignition.observe(on_value_change, names='value')'''
import numpy as np
import matplotlib.pyplot as plt
data = np.random.default_rng(12345)
oxy_nums = data.integers(low=0, high=10, size=10)

plt.bar(range(len(oxy_nums)), oxy_nums)
plt.show()