[README](README.md)

## Security
| username | password |
| -------- | -------- |
| *user* | *pass* |

## Endpoints
| desc       | cli/api                                       | web |
| ---------- | --------------------------------------------- | -------- |
| all | curl -i -k https://localhost/api   | https://localhost/ |
| all pg # | curl -i -k https://localhost/api/*int* | https://localhost/*int* |
| search name | curl -i -k https://localhost/api/name/*str* -u 'user:pass' | https://localhost/name/*str* |
| search name pg # | curl -i -k https://localhost/api/name/*int*/*str* -u 'user:pass' | https://localhost/name/*int*/*str* |
| all topic | - | https://localhost/topics/ |
| search topic | curl -i -k https://localhost/api/topic/*int* -u 'user:pass' | https://localhost/topics/*str* |
| search topic pg # | curl -i -k https://localhost/api/topic/*int*/*str* -u 'user:pass' | https://localhost/topics/*int*/*str* |
| all catagory | - | https://localhost/catagory/ |
| search catagory | curl -i -k https://localhost/api/catagory/*str*  -u 'user:pass' | https://localhost/catagory/*str* |
| search catagory pg # | curl -i -k https://localhost/api/catagory/*int*/*str*  -u 'user:pass' | https://localhost/catagory/*int*/*str* |
| all subcatagory | - | https://localhost/topics/catagory/sub/ |
| search subcatagory | curl -i -k https://localhost/api/catagory/sub/*str*  -u 'user:pass' | https://localhost/topics/catagory/sub/*str* |
| search subcatagory pg # | curl -i -k https://localhost/api/catagory/*int*/sub/*str*  -u 'user:pass' | https://localhost/catagory/*int*/sub/*str* |
| search build | curl -i -k https://localhost/api/filter/build/*str*  -u 'user:pass' | https://localhost/filter/build/*str* |
| search build pg # | curl -i -k https://localhost/api/filter/*int*/build/*str*  -u 'user:pass' | https://localhost/filter/*int*/build/*str* |
| search language | curl -i -k https://localhost/api/filter/language/*str*  -u 'user:pass' | https://localhost/filter/language/*str* |
| search language pg # | curl -i -k https://localhost/api/filter/*int*/language/*str*  -u 'user:pass' | https://localhost/filter/*int*/language/*str* |
| search platform | curl -i -k https://localhost/api/filter/platform/*str*  -u 'user:pass' | https://localhost/filter/platform/*str* |
| search platform pg # | curl -i -k https://localhost/api/filter/*int*/platform/*str*  -u 'user:pass' | https://localhost/filter/*int*/platform/*str* |
| search tech | curl -i -k https://localhost/api/filter/tech/*str*  -u 'user:pass' | https://localhost/filter/tech/*str* |
| search tech pg # | curl -i -k https://localhost/api/filter/*int*/tech/*str*  -u 'user:pass' | https://localhost/filter/*int*/tech/*str* |

## Defintions
- *int* any number 0-9
- *str* any word
