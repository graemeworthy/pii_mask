
## PII Mask

This is an an experimental implementation of field-level data masking of Personally Identifiable Information (PII) for use in Django.

### What is PII Mask?

PII Mask is a tool that helps you protect sensitive information stored in your database. It allows you to mark fields as personally identifiable, ensuring that only authorized users have access to the actual data. With PII Mask, you can enhance the privacy and security of your application without making modifications to all temp.

### Usage:

> This isn't a proper python libary (it's an experiment, after all). So, just copy the pii_mask folder.

To get started with PII Mask, follow these simple steps:

1. Install PII Mask in your Django project.
2. Identify the fields in your models that contain sensitive PII.
3. Replace those fields with the PiiField provided by PII Mask.

Here's an example to illustrate the usage:

### Configure your private fields
```
from django.db import models
from pii_mask.pii_field import PiiField

class Person(models.Model):
    name = PiiField(max_length=200)
    fav_colour = models.CharField(max_length=200)
```

By using PiiField for the name field, you ensure that any data stored in that field is protected and masked.


### Masking/Unmasking PII

PII Mask provides a simple API to control the visibility of PII. You can easily mask or unmask the protected fields as needed. Here's an example:

And this person's name is 'Alice', their favourite colour is 'blue'

```
from people.models import Person
from pii_mask.pii_context import hide_pii, show_pii

alice = Person.objects.create(name="Alice", fav_color="Blue")
bob = Person.objects.create(name="Bob", fav_color="Red")
```

Names are personally identifiable (or could be) favourite colours are not.


PII should not be visible to some users of your system.
In those cases, we can cause all PiiFields to return redactions ie: "***"

```c
from people.models import Person
from pii_mask.pii_context import hide_pii, show_pii

def look(*, viewed: Person, viewer: Person):
  """A Person can only see their own private data."""

  if viewed == viewer:
    show_pii()
  else:
    hide_pii()

  print(f"""
    This person's name is: {viewed.name}.
    Their favourite colour is: {viewed.fav_colour}
  """)
```

```
>>> look(viewed=alice, viewer=alice)

    This person's name is: Alice.
    Their favourite colour is: blue

>>> look(viewed=alice, viewer=bob)

    This person's name is: *****.
    Their favourite colour is: blue

```


This feature would allow you to selectively display PII based on user permissions, ensuring that sensitive information remains hidden from unauthorized users.

#### Privacy Middleware
To further enhance privacy protection, PII Mask provides a privacy mask middleware. By including this middleware in your Django project, PII Mask will automatically mask PII on every request.


```
# settings.py
MIDDLEWARE = [
  "pii_mask.middleware.privacy_mask.PrivacyMaskMiddleware",
]

```
