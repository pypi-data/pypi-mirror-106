# TW Complex

Repo with algorithms to divide ally villages into front and back in TW.

Underneath it is a problem of dividing a set of 2D points **A** according to the `min_radius` and `max_radius` distances from a set of other 2D points **B**, which can be solved most simply by counting the distances from each point in the first set **A** to all points in the second set **B** one by one.

# Examples (before -> after)

### Example 1

```bash
Ally: 10000 points
Enemy: 15000 points
min_radius: 1.4
max_radius: 2
```

![example1](https://raw.githubusercontent.com/rafsaf/tw-complex/main/images/Figure_1.png)

### Example 2

```bash
Ally: 2500 points
Enemy: 6000 points
min_radius: 4
max_radius: 10
```

![example2](https://raw.githubusercontent.com/rafsaf/tw-complex/main/images/Figure_2.png)

### Example 3

```bash
Ally: 20000 points
Enemy: 20000 points
min_radius: 20
max_radius: 60
```

![example3](https://raw.githubusercontent.com/rafsaf/tw-complex/main/images/Figure_3.png)

### Example 4

```bash
Ally: 20000 points
Enemy: 20000 points
min_radius: 10
max_radius: 120
```

![example4](https://raw.githubusercontent.com/rafsaf/tw-complex/main/images/Figure_4.png)
