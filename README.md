# Introduction to Python

To learn about the workshop go to the university [USOS information page](https://usosweb.uwm.edu.pl/kontroler.php?_action=katalog2/przedmioty/pokazPrzedmiot&prz_kod=2317S2-INP).

## Grades, how do they work?

- The student is working with the prepared Jupyter Notebook files (fork),
- All work is done individually by the student,
- All work should be stored in a public GitHub repository for preview,
- What is taken into consideration while grading:
   - Regularity of commits to the repository,
   - Keeping Python standards in code,
   - End exam `(you can only repeat it once)`.
   - Code quality.


## Workspace setup

You can use two python distributions for the workshops:

- Anaconda 3.7 (prefered),
- Python 3.7.

### Anaconda installation

1. Install Anaconda from [the official website](https://www.anaconda.com/products/individual),
2. Open terminal / command prompt,
3. Create a new environment (approve all pending questions):
   ```bash
   conda create -n introduction-to-python python=3.7
   ```
4. Start using the created environment:
   ```bash
   conda activate introduction-to-python
   ```
5. Install packages to be used in our workshops:
   ```bash
   conda install notebook pandas numpy matplotlib seaborn
   ```
6. To start the Jupyter server navigate to your repository folder and run:
   ```bash
   jupyter notebook
   ```

### Python installation

1. Install Python 3.7 from [the official website](https://www.python.org/downloads/release/python-370/),
2. Open terminal / command prompt,
3. Navigate to your repository folder,
4. Install `virtualenv`:
   ```bash
   pip install virtualenv
   ```
5. Create virtual environment:
   ```bash
   virtualenv introduction-to-python
   ```
6. Activate the virtual environment:
   ```bash
   # MacOS / Linux
   source introduction-to-python/bin/activate

   # Windows
   introduction-to-python\Scripts\activate
   ```
7. Install packages to be used in our workshops:
   ```bash
   pip install notebook pandas numpy matplotlib seaborn
   ```
8. To start the Jupyter server run:
   ```bash
   jupyter notebook
   ```