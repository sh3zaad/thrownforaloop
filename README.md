# thrownforaloop

A package just to practice using Bash, pushing and pulling. The functions
contained are a small collection of sorting functions as well as a select group
of recursive functions that do things from give the nth term in a fibonacci
sequence to adding all values in an array.

## Installation

To install thrownforaloop:

```bash
pip install git+https://github.com/sh3zaad/thrownforaloop.git
```

To update thrownforaloop:

```bash
pip install --upgrade git+https://github.com/sh3zaad/thrownforaloop.git
```

## Usage

```python
import thrownforaloop

thrownforaloop.sum_array([1, 2, 3]) # returns 6
thrownforaloop.fibonacci(2) # returns 1
thrownforaloop.factorial(3) # returns 6
thrownforaloop.reverse('word') # returns 'drow'
thrownforaloop.bubble_sort([3, 5, 2, 1, 10]) # returns [1, 2, 3, 5, 10]
thrownforaloop.merge_sort([12, 5, 9, 3, 8]) # returns [3, 5, 8, 9, 12]
thrownforaloop.quick_sort([g, u, k, e, b, a]) # returns [a, b, e, g, k, u]
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)
