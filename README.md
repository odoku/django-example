# Django のサンプル


## 環境構築

```
# テスト環境の起動
docker-compose up

# DB のマイグレーション
docker exec -it django-example /app/manage.py migrate

# 管理画面のユーザーを追加
docker exec -it django-example /app/manage.py createsuperuser
```


## 操作方法

### DBスキーマの変更

モデルクラスを追加・変更ののち、以下のコマンドを実行。

```
docker exec -it django-example /app/manage.py makemigrations [appname, ...]
docker exec -it django-example /app/manage.py migrate
```

マイグレーションを戻したい場合は以下の様にする。

```
# 001番ばで戻す
docker exec -it django-example /app/manage.py migrate [appname] 001

# マイグレーションが1つも反映されていない状態に戻す
docker exec -it django-example /app/manage.py migrate [appname] zero
```

### テストの実行

```
docker exec -it django-example py.test
```
