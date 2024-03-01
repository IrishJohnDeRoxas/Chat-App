-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
-- -----------------------------------------------------
-- Schema flask_chat_app
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema flask_chat_app
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `flask_chat_app` DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci ;
USE `flask_chat_app` ;

-- -----------------------------------------------------
-- Table `flask_chat_app`.`alembic_version`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `flask_chat_app`.`alembic_version` (
  `version_num` VARCHAR(32) NOT NULL,
  PRIMARY KEY (`version_num`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `flask_chat_app`.`room`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `flask_chat_app`.`room` (
  `room_id` INT NOT NULL AUTO_INCREMENT,
  `room_name` VARCHAR(255) NOT NULL,
  `owner` TEXT NOT NULL,
  PRIMARY KEY (`room_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 7
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `flask_chat_app`.`room_messages`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `flask_chat_app`.`room_messages` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `room_id` INT NULL DEFAULT NULL,
  `sender` TEXT NOT NULL,
  `message` TEXT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `room_id` (`room_id` ASC) VISIBLE,
  CONSTRAINT `room_messages_ibfk_1`
    FOREIGN KEY (`room_id`)
    REFERENCES `flask_chat_app`.`room` (`room_id`))
ENGINE = InnoDB
AUTO_INCREMENT = 10
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


-- -----------------------------------------------------
-- Table `flask_chat_app`.`users`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `flask_chat_app`.`users` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `username` VARCHAR(255) NOT NULL,
  `hashed_password` TEXT NOT NULL,
  `first_name` TEXT NOT NULL,
  `last_name` TEXT NOT NULL,
  `age` INT NOT NULL,
  PRIMARY KEY (`id`))
ENGINE = InnoDB
AUTO_INCREMENT = 8
DEFAULT CHARACTER SET = utf8mb4
COLLATE = utf8mb4_0900_ai_ci;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
