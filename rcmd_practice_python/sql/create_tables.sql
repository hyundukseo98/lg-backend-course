-- 영화 테이블 생성
CREATE TABLE IF NOT EXISTS `contents` (
  `content_id` INT NOT NULL AUTO_INCREMENT,
  `type` VARCHAR(100) NOT NULL,
  `title` VARCHAR(255) NOT NULL,
  `year` INT NOT NULL,
  `genre` VARCHAR(100) NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`content_id`),
  INDEX `idx_type` (`type`),
  INDEX `idx_year` (`year`),
  INDEX `idx_genre` (`genre`)
) ENGINE = InnoDB DEFAULT CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

-- 사용자 테이블 생성
CREATE TABLE IF NOT EXISTS `users` (
  `user_id` INT NOT NULL AUTO_INCREMENT,
  `name` VARCHAR(100) NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `updated_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`user_id`),
  INDEX `idx_name` (`name`)
) ENGINE = InnoDB DEFAULT CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;

-- 추천 테이블 생성
CREATE TABLE IF NOT EXISTS `rcmd_user_content` (
  `user_id` INT NOT NULL,
  `content_id` INT NOT NULL,
  `created_at` DATETIME NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`user_id`, `content_id`),
  CONSTRAINT `fk_rcmd_user` FOREIGN KEY (`user_id`) REFERENCES `users`(`user_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `fk_rcmd_content` FOREIGN KEY (`content_id`) REFERENCES `contents`(`content_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB DEFAULT CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;