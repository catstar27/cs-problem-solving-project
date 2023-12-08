import atexit
import os
from view import View

pi = 3.14159
frequencies = ["Low", "Mid", "High", "All"]
# making use of color palette from here: https://colorhunt.co/palette/363062435585818fb4f5e8c7


def set_rt_graph(num):
    if app.is_file_loaded:
        app.current_rt_graph_index += num
        app.current_rt_graph_index %= 4
        if frequencies[app.current_rt_graph_index] != "All":
            app.rt_graph.plot_waveform(frequencies[app.current_rt_graph_index])
        else:
            app.rt_graph.plot_all()
        app.rt_buttons.update_graph_label(frequencies[app.current_rt_graph_index])


def update_rt_display():
    app.rt_display.setText(f"RT60 Value: {round(abs(app.rt_graph.rt60), 2)} seconds")


def update_max_freq_display():
    app.max_freq_display.setText(f"Max Frequency: {round(app.rt_graph.value_of_max, 2)} Hz")


def file_loaded():  # updates the label of audio duration after the file is loaded
    app.length_message.setText(f"Audio Duration: {app.file_load_frame.file.duration} seconds")
    app.waveform.plot_waveform()
    app.rt_graph.plot_waveform(frequencies[app.current_rt_graph_index])
    app.rt_buttons.update_graph_label(frequencies[app.current_rt_graph_index])
    app.spectrogram.plot_spectrogram()
    app.is_file_loaded = True


def filepath_changed():  # updates file load frame filepath to the filepath in file select frame
    app.file_load_frame.filepath = app.file_select_frame.file_path_label.toPlainText()


def exit_handler():  # runs on exit, deleting the temporary wav file
    if os.path.exists("file.wav"):
        os.remove("file.wav")


if __name__ == "__main__":
    # app preparation
    atexit.register(exit_handler)
    app = View()

    # link signals
    app.rt_graph.rt60_changed.connect(update_rt_display)
    app.rt_graph.max_freq_changed.connect(update_max_freq_display)
    app.rt_buttons.next_button.clicked.connect(lambda: set_rt_graph(1))
    app.rt_buttons.prev_button.clicked.connect(lambda: set_rt_graph(-1))
    app.file_select_frame.file_path_label.textChanged.connect(filepath_changed)
    app.file_load_frame.load_signal.connect(file_loaded)

    app.window.show()
    app.exec()
