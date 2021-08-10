[![Python][python-shield]][python-url]
[![Documentation][documentation-shield]][documentation-url]
[![Github][github-shield]][github-url]
[![LinkedIn][linkedin-shield]][linkedin-url]


<br />
<p align="center">
  <h3 align="center">Constrained Gradient Boosting</h3>

  <p align="center">
    Template Multi Level Python Package
    <br />
  </p>



<!-- ABOUT THE PROJECT -->
## About The Project
This is a template project for creating multi-level python package. For multi level python package, in each folder you
should insert an empty `__ini__.py`. Then, in the main folder, you should import the package name (which is the same
as main folder name), then import files from sub-folders. Using this, you can import functions or classes in subfolders
by `package_name.function`

<!-- GETTING STARTED -->
## Getting Started

To test, cd to the `template_multi_level` main directory, where the `setup.py` is:
  ```sh
  cd ../template_multi_level
  ```

Then:
```sh
   pip install -e.
   ```

In Python:

   ```sh
   import template_multi_level as tml
   tml.function_file1()
   ```

Output:

   ```sh
   you have called function from file 1 in level 2
   3
   ```

<!-- CONTACT -->
## Contact

Feel free to make the template better, and ask questions:

Maryam Bahrami - maryami_66@yahoo.com

Project Link: [https://github.com/maryami66/template_multi_level](https://github.com/your_username/repo_name)





<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[python-shield]: https://img.shields.io/badge/Python-v3.7-blue
[python-url]: https://www.python.org/downloads/release/python-370/
[documentation-shield]: https://img.shields.io/badge/docs-passing-brightgreen
[documentation-url]: https://github.com/maryami66/constrained_gb/doc/build/html/index.html
[github-shield]: https://img.shields.io/badge/status-stable-brightgreen
[github-url]: https://github.com/maryami66/template_multi_level
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/maryam-bahrami-a6558496/
