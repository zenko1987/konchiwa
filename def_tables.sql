-- 1.��ʃ��[�U���쐬����i���[�U�����ɂ���ꍇ�́A2����j
-- ��`
CREATE USER ronbun_user@'%' IDENTIFIED BY 'Dev_1648';

-- �m�F
select host, user from mysql.user;

-- 2.DB���쐬����
-- DB��`
CREATE DATABASE ronbun default character set utf8 COLLATE utf8_general_ci;

-- �A�N�Z�X�ݒ�
GRANT ALL ON ronbun.* to ronbun_user@'%' identified BY 'Dev_1648';

------------------------------------------------------------ �����܂�root���[�U

-- �m�F
-- exit���āA��ʃ��[�U�Őڑ��ł��邩�H
mysql -u ronbun_user -pDev_1648 ronbun --default-character-set=utf8;



-- M_���[�U�[(��)
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