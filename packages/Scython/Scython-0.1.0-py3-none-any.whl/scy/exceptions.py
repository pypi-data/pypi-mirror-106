# Tokenizer exceptions
UNEXPECTED_CHARACTER = 'Unexpected character.'
RESERVED_KEYWORD = 'Reserved keyword %r.'
INVALID_HEX_STRING = 'Invalid hex string %r.'
MULTILINE_STRINGS_NOT_SUPPORTED = 'Multiline strings not supported.'
EOF_DURING_STRING = 'EOF reached during string.'
UNEXPECTED_EOF = 'Unexpected EOF.'

# Parser exceptions
INVALID_ASSIGNMENT = 'Invalid assignment target.'
ITERATION_INVALID_ASSIGNMENT = 'Invalid assignment target for iteration.'
EXPECT_EXPRESSOIN = 'Expect expression.'
INVALID_ASYNC = 'Async keyword not supported with %r statements.'
INVALID_ASYNC_EXPR = 'Async keyword not supported with expression statements.'
INVALID_ASYNC_FOR = "Async for loops only compatible with iteration (using ':' syntax)."
EXPECT_PROPERTY_NAME = "Expect property name after '.'."
