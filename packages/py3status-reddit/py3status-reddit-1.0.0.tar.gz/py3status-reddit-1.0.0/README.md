# py3status-reddit

A py3status module showing reddit unread messages.

## install

```
pip install py3status-reddit
```

## configuration

* `format`: output format (default `reddit: {count}`)
* `cache_timeout`: how often to refresh the information

A fancier format could be achieved using Font Awesome:

```
format = '\?if=!count=0 <span color="#FF5700" font_family="FontAwesome">\uf281 <span font_weight="heavy">{count}</span></span>|'
```

![](fancy_count.png)

## first time launch

The first time you launch this module, you will have to
authorize it via an OAuth flow you can start by clicking on it.
