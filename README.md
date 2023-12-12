# Домашнее задание №2
Для версионирования данных использую `git-lfs`

## Что выполнил
```shell
brew install git-lfs

git lfs install
git lfs track "*.csv"
git add .gitattributes
```

---
## Как получить данные
```shell
git clone <URL>
git lfs pull
```

## Как добавлять/ обновлять данные

```shell
git lfs track <FILE PATH> # если формат добавляемого файла не отслеживается

git add <FILE PATH>
git commit -m <COMMIT MESSAGE> 
git push origin main
```

