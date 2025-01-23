# pypp
Python PreProcessor. Annotate python code with various #comments like #PYPP#DELETE#.

This allows to remove certain lines of code in production deployments,
to squeeze out performance.

## Usage

`python -m pypp --recursive files or dirs`

## Directives

Only 3 directives are implemented:

 - `#PYPP#DELETE#` deletes the line this comment appears in.
 - `#PYPP#BEGIN#` starts a deletion block.
 - `#PYPP#END#` ends a deletion block.

No sanity checks!

### LICENSE

[MIT](./LICENSE)

(c)2024 gizmore@wechall.net + chappy
