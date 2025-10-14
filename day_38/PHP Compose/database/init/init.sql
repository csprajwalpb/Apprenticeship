-- Database initialization script for all applications
-- This script creates all necessary databases and users

-- Create databases
CREATE DATABASE IF NOT EXISTS springdb;
CREATE DATABASE IF NOT EXISTS phpdb;
CREATE DATABASE IF NOT EXISTS nodedb;

-- Create users for each application
CREATE USER IF NOT EXISTS 'springuser'@'%' IDENTIFIED BY 'springpass';
CREATE USER IF NOT EXISTS 'phpuser'@'%' IDENTIFIED BY 'phppass';
CREATE USER IF NOT EXISTS 'nodeuser'@'%' IDENTIFIED BY 'nodepass';

-- Grant privileges
GRANT ALL PRIVILEGES ON springdb.* TO 'springuser'@'%';
GRANT ALL PRIVILEGES ON phpdb.* TO 'phpuser'@'%';
GRANT ALL PRIVILEGES ON nodedb.* TO 'nodeuser'@'%';

-- Flush privileges
FLUSH PRIVILEGES;

-- Create tables for each database
USE springdb;
CREATE TABLE IF NOT EXISTS users (
    id BIGINT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

USE phpdb;
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

USE nodedb;
CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL UNIQUE,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);