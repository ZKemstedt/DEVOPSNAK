

# regex

## meta characters
```regex
^   beginning of text
$   end of text
.   any character
*   zero of more
+   one or more
?   zero or one
-
|   or
\
[   
]
{
}
(
)
```

## quantifiers
```regex
?       zero or one
*       zero or more
+       one or more
{n}     exactly n
{n,}    at least n
{,m}    max m
{n,m}   at least n, max m
```

## classes
```regex
[abc]       one of 'a', 'b' or 'c'
[a-c]       a to b
[a-cd]      a to b and d
[^0-9]      NOT 0-9
[[:word]]   'word characters'
[[:space:]] 'whitespace'

```