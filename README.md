# Machine learning workshop

This is a workshop for Python developpers with no previous experience in Machine Learning (but some programming knowledge). 

To run it, you have a few options: 

1. If you like to use Docker, you can just use 

    `make` 
    
    This will create a Docker container with everything you need. There will be a link in the output, follow it in your browser. From there click on the `work` folder and open the workshop (`Workshop notebook.ipynb`)
2. If you'll rather use conda, install miniconda (instructions [here](https://conda.io/miniconda.html)). 
    Then run
    
    `conda env create -n ml-workshop -f requirements.yml`
    
    and
    `conda activate ml-workshop` to activate the environement. 
    Then run `jupyter notebook` to start the notebook.
3. If you're more of a pip person, create a virtual env, then:

    `pip install -r requirements.txt`.
    
    Then run `jupyter notebook` to start the notebook.