-- 1.一般ユーザを作成する（ユーザが既にある場合は、2から）
-- 定義
CREATE USER ronbun_user@'%' IDENTIFIED BY 'Dev_1648';

-- 確認
select host, user from mysql.user;

-- 2.DBを作成する
-- DB定義
CREATE DATABASE ronbun default character set utf8 COLLATE utf8_general_ci;

-- アクセス設定
GRANT ALL ON ronbun.* to ronbun_user@'%' identified BY 'Dev_1648';

------------------------------------------------------------ ここまでrootユーザ

-- 確認
-- exitして、一般ユーザで接続できるか？
mysql -u ronbun_user -pDev_1648 ronbun --default-character-set=utf8;



-- M_ユーザー(例)
DROP TABLE IF EXISTS q_cb.m_users;
CREATE TABLE q_cb.m_users(
 user_id INTEGER UNSIGNED NOT NULL AUTO_INCREMENT
,user_nm VARCHAR(35) NOT NULL
,update_id INTEGER NOT NULL
,created DATETIME NOT NULL
,modified DATETIME NOT NULL
,deleted_f TINYINT(1) NOT NULL
,CONSTRAINT PRIMARY KEY (user_id)
) ENGINE = InnoDB
;