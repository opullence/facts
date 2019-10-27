# Facts
Facts are used to represent data

## Declare a `Person`

```python

> from opulence.facts.person import Person
> john_snow = Person()
> john_snow.is_valid()
False
> john_snow = Person(firstname="John", lastname="Snow")
> john_snow.is_valid()
True
> john_snow.get_fields()
...
```

## Play with jobs

```python
> from opulence.common.job import Job
> from opulence.facts.person import Person
> john_snow = Person(lastname="Sohn", firstname="Jnow")
> arya_stark = Person(lastname="Sarya", firstname="Atark")

> todo = Job(john_snow)
> todo.output = arya_stark
> todo.to_json()


```
