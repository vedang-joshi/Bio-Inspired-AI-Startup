# Predicting gradual and sharp temperature drops for use in preventing cold water shocks

This repository contains the Python code to reproduce the proposed neural network in the coursework for [EMATM0029: Bio-Inspired Artificial Intelligence](https://www.bris.ac.uk/unit-programme-catalogue/UnitDetails.jsa?ayrCode=21%2F22&unitCode=EMATM0029). A saved version of this neural net may be found at Neural Net v1.0/. The Jupyter Notebook to run may be found at Neural Net v1.0/ - there are no dependencies on any other python file. This Jupyter Notebook also produces the plots found in Neural Net v1.0/Accuracy plots/.

In this work, we develop a dense neural network to predict the gradual and sharp temperature drops that may occur when a person steps into cold water suddenly. We propose a startup to develop such a product with the proposed neural network at the core of the implementation. We used a [Raspberry Pico](https://www.cytron.io/p-maker-pi-pico) microcontroller, with a [Grove Temperature sensor](https://wiki.seeedstudio.com/Grove-Temperature_Sensor_V1.2/) to detect the ambient temperature. The data used to train the neural net was collected with this setup for trials lasting 1.5 mins. The device was set to collect the ambient temperature for 20 - 30 s before being placed in a freezer with minimum temperature -18 C. This was done for 33 trials. The device started collecting data starting from temperatures ranging from 7 C to 20 C, and the sharp temperature drop was recorded. A similar experiment was conducted but the device setup was placed in the fridge with the minimum temperature reaching 4 C.

## Requirements
This code requires Python 3.8. [Anaconda](https://www.anaconda.com/distribution/) is recommended as the default Python environment and package manager to make the setup easy.
### Setting Up a Virtual Environment
- After setting up Anaconda, in your Anaconda prompt/ Terminal:
```bash
$ conda update conda
$ conda update --all
```
- You may create a new [virtual environment](https://docs.python.org/3/tutorial/venv.html) (called `env`) as follows:
```bash
$ conda create -n env python=3.8 anaconda
```
### Dependencies

- Install python external dependencies after activating `env`: 
```bash
$ conda activate env
$ pip install -r requirements.txt
```
### Dopri/Radau and AUTO interface requirements
- Install [swig](http://www.swig.org): 
```bash
$ conda install -c anaconda swig
```

## Notes
Reproduction of figure 6 may be done using the corresponding code but involves parallelisation and the use of multiple cores. For ease of reproduction, we recommend downloading 'max_values_list_Z.pkl' and 'vm3_value_list.pkl' and instead running 'figure_6_after_parallel.py'.

## Author

* **Vedang Joshi**  - [Personal Page](https://vedang-joshi.github.io)


## License

This project is licensed under the GNU General Public License v3.0 - see the [LICENSE.md](LICENSE.md) file for details
