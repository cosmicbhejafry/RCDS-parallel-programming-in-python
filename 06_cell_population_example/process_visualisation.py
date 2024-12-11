import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def visualise_realisation_runtimes(realisation_df, filename):  
    fig, ax = plt.subplots()
    process_numbers = [int(process_number) for process_number in realisation_df['process'].unique()]
    process_numbers.sort()

    colour_palette = ['orange', 'blue', 'green', 'red', 'purple', 'brown', 'pink', 'grey', 'white', 'yellow']

    for process_number in process_numbers:
        process_label = f'Process {process_number}'
        process_df = realisation_df[realisation_df['process'] == process_number]
        run_times = process_df['run_time'].values
        realisation_numbers = process_df['number'].values
        lefts = np.cumsum(run_times)
        lefts = np.insert(lefts[:-1], 0, 0)
        colours = colours = [colour_palette[realisation_number % len(colour_palette)] for realisation_number in realisation_numbers]
        
        ax.barh(process_label, run_times, left=lefts, color=colours, edgecolor='black')
        
        x_min, x_max = ax.get_xlim()
        label_threshold = 0.03 * (x_max - x_min)

        for i, run_time in enumerate(run_times):
            if run_time > label_threshold:
                ax.text(lefts[i] + run_time / 2, process_label, realisation_numbers[i], ha='center', va='center')

    ax.set_xlabel('Run Time (s)')
        

    fig.savefig(filename, bbox_inches='tight')