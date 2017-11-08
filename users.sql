/*
CREATE TABLE `users` (
	`id` INT(11) NOT NULL AUTO_INCREMENT,
	`uid` VARCHAR(50) NOT NULL,
	`upw` VARCHAR(50) NULL DEFAULT NULL,
	`name` VARCHAR(50) NULL DEFAULT NULL,
	`regdate` TIMESTAMP NOT NULL DEFAULT '',
	PRIMARY KEY (`id`),
	UNIQUE INDEX `uid` (`uid`)
)
COMMENT='회원정보'
ENGINE=InnoDB
;
*/
-- 회원정보 입력
-- INSERT INTO `python`.`users` (`uid`, `upw`, `name`) 
-- VALUES ('nia', '1234', '파이썬');
-- 회원정보 조회
SELECT `id`, `uid`, `upw`, `name`, `regdate` FROM `python`.`users` ;
-- 로그인
SELECT * FROM USERS WHERE uid='' and upw='';