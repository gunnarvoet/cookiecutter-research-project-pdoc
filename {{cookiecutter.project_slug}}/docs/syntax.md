# Syntax Examples

## header 1

### header 2

try this.[^ref]
[^ref]: Some footnote text

> quote

    another test of some block quote

this is some inline math $a=1$ or 

$$
\int_0^1 z dz
$$

Here is a link to the [New York Times](https://nytimes.com)

% ![image](../fig/testbild.jpg)


```python
print('this is python')

def test(a):
    return a + 1
```

This is the figure environment:
```{figure} ../fig/testbild.jpg
:figwidth: 800px
:width: 800px
Caption with markdown **hello**.
```

The figure environment with a name that can be referenced:
```{figure} ../fig/testbild.jpg
:figwidth: 800px
:name: fig-test
Caption with markdown **hello**.
```

Include image via html tag; here we can define a maximum width and the figure resizes:
<img alt="image via html tag" src="../fig/testbild.jpg" style="max-width:400px;width:100%">

A simple way of showing an image (figure resizes):
![sketch](../fig/testbild.jpg)

Some more text.

Here is a reference to {numref}`fig-test`. We can also [link](fig-sketch) to figures in this way, across pages.

Refer to {class}`{{ cookiecutter.project_slug }}.io`.
