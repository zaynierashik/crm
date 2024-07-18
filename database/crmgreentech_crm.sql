-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: localhost:3306
-- Generation Time: Jul 18, 2024 at 02:50 PM
-- Server version: 8.0.37-cll-lve
-- PHP Version: 8.3.8

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `crmgreentech_crm`
--

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` bigint NOT NULL,
  `group_id` int NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add brand', 1, 'add_brand'),
(2, 'Can change brand', 1, 'change_brand'),
(3, 'Can delete brand', 1, 'delete_brand'),
(4, 'Can view brand', 1, 'view_brand'),
(5, 'Can add company', 2, 'add_company'),
(6, 'Can change company', 2, 'change_company'),
(7, 'Can delete company', 2, 'delete_company'),
(8, 'Can view company', 2, 'view_company'),
(9, 'Can add partner', 3, 'add_partner'),
(10, 'Can change partner', 3, 'change_partner'),
(11, 'Can delete partner', 3, 'delete_partner'),
(12, 'Can view partner', 3, 'view_partner'),
(13, 'Can add sector', 4, 'add_sector'),
(14, 'Can change sector', 4, 'change_sector'),
(15, 'Can delete sector', 4, 'delete_sector'),
(16, 'Can view sector', 4, 'view_sector'),
(17, 'Can add service', 5, 'add_service'),
(18, 'Can change service', 5, 'change_service'),
(19, 'Can delete service', 5, 'delete_service'),
(20, 'Can view service', 5, 'view_service'),
(21, 'Can add contact', 6, 'add_contact'),
(22, 'Can change contact', 6, 'change_contact'),
(23, 'Can delete contact', 6, 'delete_contact'),
(24, 'Can view contact', 6, 'view_contact'),
(25, 'Can add staff', 7, 'add_staff'),
(26, 'Can change staff', 7, 'change_staff'),
(27, 'Can delete staff', 7, 'delete_staff'),
(28, 'Can view staff', 7, 'view_staff'),
(29, 'Can add requirement', 8, 'add_requirement'),
(30, 'Can change requirement', 8, 'change_requirement'),
(31, 'Can delete requirement', 8, 'delete_requirement'),
(32, 'Can view requirement', 8, 'view_requirement'),
(33, 'Can add transaction', 9, 'add_transaction'),
(34, 'Can change transaction', 9, 'change_transaction'),
(35, 'Can delete transaction', 9, 'delete_transaction'),
(36, 'Can view transaction', 9, 'view_transaction'),
(37, 'Can add log entry', 10, 'add_logentry'),
(38, 'Can change log entry', 10, 'change_logentry'),
(39, 'Can delete log entry', 10, 'delete_logentry'),
(40, 'Can view log entry', 10, 'view_logentry'),
(41, 'Can add permission', 11, 'add_permission'),
(42, 'Can change permission', 11, 'change_permission'),
(43, 'Can delete permission', 11, 'delete_permission'),
(44, 'Can view permission', 11, 'view_permission'),
(45, 'Can add group', 12, 'add_group'),
(46, 'Can change group', 12, 'change_group'),
(47, 'Can delete group', 12, 'delete_group'),
(48, 'Can view group', 12, 'view_group'),
(49, 'Can add user', 13, 'add_user'),
(50, 'Can change user', 13, 'change_user'),
(51, 'Can delete user', 13, 'delete_user'),
(52, 'Can view user', 13, 'view_user'),
(53, 'Can add content type', 14, 'add_contenttype'),
(54, 'Can change content type', 14, 'change_contenttype'),
(55, 'Can delete content type', 14, 'delete_contenttype'),
(56, 'Can view content type', 14, 'view_contenttype'),
(57, 'Can add session', 15, 'add_session'),
(58, 'Can change session', 15, 'change_session'),
(59, 'Can delete session', 15, 'delete_session'),
(60, 'Can view session', 15, 'view_session');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(150) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$720000$PiKR6EezSxGoFPZKUUpg3U$1uuAeB102jd/3T/H+wNRcrPi5ZeIo8pAFzuzQLfR+ug=', '2024-07-18 03:16:56.783096', 1, 'crmgreentech', '', '', 'crm@greentechconcern.com', 1, 1, '2024-07-12 10:25:28.518844');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` bigint NOT NULL,
  `user_id` int NOT NULL,
  `group_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` bigint NOT NULL,
  `user_id` int NOT NULL,
  `permission_id` int NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int DEFAULT NULL,
  `user_id` int NOT NULL
) ;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2024-07-14 09:22:56.036506', '6', 'Suman Pokhrel', 2, '[{\"changed\": {\"fields\": [\"Company\"]}}]', 6, 1),
(2, '2024-07-14 09:29:15.898956', '13', 'Global IME Bank', 1, '[{\"added\": {}}]', 9, 1),
(3, '2024-07-14 09:30:57.398486', '4', 'IT', 1, '[{\"added\": {}}]', 4, 1),
(4, '2024-07-14 09:31:31.308191', '5', 'Cyber Secured India', 1, '[{\"added\": {}}]', 2, 1),
(5, '2024-07-14 09:32:41.103953', '8', 'Nikhil Santosh Mahadeshwar', 1, '[{\"added\": {}}]', 6, 1),
(6, '2024-07-14 09:32:59.192670', '2', 'MoU', 1, '[{\"added\": {}}]', 5, 1),
(7, '2024-07-14 09:34:22.736616', '5', 'Cyber Secured India', 2, '[]', 2, 1),
(8, '2024-07-14 09:34:53.429585', '5', 'Cyber Secured India', 3, '', 2, 1),
(9, '2024-07-14 09:37:54.208922', '1', 'Undefined', 1, '[{\"added\": {}}]', 3, 1),
(10, '2024-07-14 09:37:59.112854', '6', 'Thomas Cook India Pvt. Ltd.', 2, '[{\"changed\": {\"fields\": [\"Company Name\", \"Sector\", \"Via\", \"Partner Name\"]}}]', 2, 1),
(11, '2024-07-14 09:38:59.281738', '9', 'Vikram Jethe Rajeshwari', 2, '[{\"changed\": {\"fields\": [\"Contact Name\", \"Email\"]}}]', 6, 1),
(12, '2024-07-14 09:57:25.234314', '29', 'Sanathan Textiles Limited', 2, '[{\"changed\": {\"fields\": [\"Remark\"]}}]', 9, 1),
(13, '2024-07-14 10:01:27.783456', '33', 'EXL', 2, '[{\"changed\": {\"fields\": [\"Remark\"]}}]', 9, 1),
(14, '2024-07-14 10:13:15.598702', '37', 'InfoDevelopers Pvt. Ltd.', 2, '[{\"changed\": {\"fields\": [\"Remark\"]}}]', 9, 1),
(15, '2024-07-14 10:42:46.018276', '14', 'Institute of Cost Accountant of India', 2, '[{\"changed\": {\"fields\": [\"Referral Name\"]}}]', 2, 1),
(16, '2024-07-14 10:54:15.136293', '75', 'ICICI Bank', 2, '[{\"changed\": {\"fields\": [\"Remark\"]}}]', 9, 1),
(17, '2024-07-14 10:54:44.031454', '75', 'ICICI Bank', 2, '[]', 9, 1),
(18, '2024-07-14 11:01:26.905381', '76', 'Chandigarh University', 2, '[{\"changed\": {\"fields\": [\"Action\", \"Remark\"]}}]', 9, 1),
(19, '2024-07-15 02:24:49.007243', '24', 'Manoj Poudel', 2, '[]', 6, 1),
(20, '2024-07-15 02:26:02.626578', '3', 'Government', 3, '', 4, 1),
(21, '2024-07-15 02:26:45.994508', '20', 'Federation of Nepalese Chambers of Commerce & Industries (FNCCI)', 2, '[{\"changed\": {\"fields\": [\"Sector\"]}}]', 2, 1),
(22, '2024-07-15 02:26:53.907254', '3', 'Ministry of Information Communication & Technology', 2, '[{\"changed\": {\"fields\": [\"Sector\"]}}]', 2, 1),
(23, '2024-07-18 03:17:45.095403', '106', 'Excelligent Consulting Services (P) Ltd.', 2, '[{\"changed\": {\"fields\": [\"Action\", \"Remark\"]}}]', 9, 1),
(24, '2024-07-18 03:21:40.079278', '106', 'Excelligent Consulting Services (P) Ltd.', 2, '[{\"changed\": {\"fields\": [\"Remark\"]}}]', 9, 1),
(25, '2024-07-18 03:21:44.607467', '107', 'Excelligent Consulting Services (P) Ltd.', 2, '[{\"changed\": {\"fields\": [\"Remark\"]}}]', 9, 1),
(26, '2024-07-18 03:29:22.604259', '24', 'Wonder Cement', 2, '[{\"changed\": {\"fields\": [\"Via\", \"Partner Name\"]}}]', 2, 1),
(27, '2024-07-18 03:29:53.049497', '1', 'Partner Undefined', 2, '[{\"changed\": {\"fields\": [\"Partner Name\"]}}]', 3, 1),
(28, '2024-07-18 03:33:16.188507', '114', 'Wonder Cement', 2, '[{\"changed\": {\"fields\": [\"Remark\"]}}]', 9, 1),
(29, '2024-07-18 03:43:24.129246', '123', 'Prabhu Technology', 2, '[{\"changed\": {\"fields\": [\"Remark\"]}}]', 9, 1),
(30, '2024-07-18 03:43:38.383914', '123', 'Prabhu Technology', 2, '[{\"changed\": {\"fields\": [\"Remark\"]}}]', 9, 1),
(31, '2024-07-18 03:43:46.130802', '123', 'Prabhu Technology', 2, '[{\"changed\": {\"fields\": [\"Remark\"]}}]', 9, 1),
(32, '2024-07-18 03:48:10.900263', '125', 'Credit Information Bureau Nepal', 2, '[{\"changed\": {\"fields\": [\"Remark\"]}}]', 9, 1),
(33, '2024-07-18 03:51:22.609876', '128', 'NIC Asia Bank Ltd.', 2, '[{\"changed\": {\"fields\": [\"Remark\"]}}]', 9, 1),
(34, '2024-07-18 03:55:56.066865', '137', 'Log Us Business Systems Pvt. Ltd.', 2, '[{\"changed\": {\"fields\": [\"Remark\"]}}]', 9, 1),
(35, '2024-07-18 03:58:12.907650', '140', 'Nabil Bank', 2, '[{\"changed\": {\"fields\": [\"Remark\"]}}]', 9, 1),
(36, '2024-07-18 04:25:30.948669', '37', 'Mipandeep Singh', 1, '[{\"added\": {}}]', 6, 1),
(37, '2024-07-18 04:28:22.544315', '28', 'Product', 1, '[{\"added\": {}}]', 8, 1),
(38, '2024-07-18 04:29:39.680573', '141', 'All India Council for Technical Education (AICTE)', 1, '[{\"added\": {}}]', 9, 1),
(39, '2024-07-18 04:29:45.144521', '141', 'All India Council for Technical Education (AICTE)', 2, '[{\"changed\": {\"fields\": [\"Created By\"]}}]', 9, 1),
(40, '2024-07-18 04:31:10.619889', '142', 'All India Council for Technical Education (AICTE)', 1, '[{\"added\": {}}]', 9, 1),
(41, '2024-07-18 04:31:24.531451', '142', 'All India Council for Technical Education (AICTE)', 2, '[{\"changed\": {\"fields\": [\"Remark\"]}}]', 9, 1),
(42, '2024-07-18 08:15:47.847273', '146', 'Yantra Solutions', 2, '[{\"changed\": {\"fields\": [\"Remark\"]}}]', 9, 1),
(43, '2024-07-18 08:19:59.301995', '150', 'Kimerlite Commerce', 2, '[{\"changed\": {\"fields\": [\"Remark\"]}}]', 9, 1),
(44, '2024-07-18 08:22:43.014154', '34', 'NDTV', 2, '[{\"changed\": {\"fields\": [\"Company Name\", \"Sector\", \"Address\", \"City\", \"Via\", \"Partner Name\"]}}]', 2, 1),
(45, '2024-07-18 08:23:16.439976', '40', 'Jaskirat Singh Bedi', 2, '[{\"changed\": {\"fields\": [\"Contact Name\", \"Email\"]}}]', 6, 1),
(46, '2024-07-18 08:28:24.325165', '155', 'FICCI', 2, '[{\"changed\": {\"fields\": [\"Remark\"]}}]', 9, 1),
(47, '2024-07-18 08:53:47.274423', '40', 'Product', 1, '[{\"added\": {}}]', 8, 1),
(48, '2024-07-18 08:55:02.313850', '168', 'Ministry of Information Communication & Technology', 1, '[{\"added\": {}}]', 9, 1),
(49, '2024-07-18 08:55:47.603396', '169', 'Ministry of Information Communication & Technology', 1, '[{\"added\": {}}]', 9, 1),
(50, '2024-07-18 08:57:38.723397', '41', 'Product', 1, '[{\"added\": {}}]', 8, 1),
(51, '2024-07-18 08:59:12.924861', '170', 'Indian Center for Policy Research & Development ', 1, '[{\"added\": {}}]', 9, 1),
(52, '2024-07-18 08:59:19.158557', '170', 'Indian Center for Policy Research & Development ', 2, '[{\"changed\": {\"fields\": [\"Created By\"]}}]', 9, 1),
(53, '2024-07-18 08:59:22.910013', '169', 'Ministry of Information Communication & Technology', 2, '[]', 9, 1),
(54, '2024-07-18 08:59:26.283224', '168', 'Ministry of Information Communication & Technology', 2, '[]', 9, 1),
(55, '2024-07-18 08:59:29.634637', '167', 'Kumari Bank Limited', 2, '[]', 9, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(10, 'admin', 'logentry'),
(12, 'auth', 'group'),
(11, 'auth', 'permission'),
(13, 'auth', 'user'),
(14, 'contenttypes', 'contenttype'),
(1, 'resecurityapp', 'brand'),
(2, 'resecurityapp', 'company'),
(6, 'resecurityapp', 'contact'),
(3, 'resecurityapp', 'partner'),
(8, 'resecurityapp', 'requirement'),
(4, 'resecurityapp', 'sector'),
(5, 'resecurityapp', 'service'),
(7, 'resecurityapp', 'staff'),
(9, 'resecurityapp', 'transaction'),
(15, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` bigint NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2024-07-12 10:18:26.858691'),
(2, 'auth', '0001_initial', '2024-07-12 10:18:28.401189'),
(3, 'admin', '0001_initial', '2024-07-12 10:18:28.702960'),
(4, 'admin', '0002_logentry_remove_auto_add', '2024-07-12 10:18:28.712547'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2024-07-12 10:18:28.728421'),
(6, 'contenttypes', '0002_remove_content_type_name', '2024-07-12 10:18:28.847411'),
(7, 'auth', '0002_alter_permission_name_max_length', '2024-07-12 10:18:28.930918'),
(8, 'auth', '0003_alter_user_email_max_length', '2024-07-12 10:18:28.959880'),
(9, 'auth', '0004_alter_user_username_opts', '2024-07-12 10:18:28.973384'),
(10, 'auth', '0005_alter_user_last_login_null', '2024-07-12 10:18:29.059992'),
(11, 'auth', '0006_require_contenttypes_0002', '2024-07-12 10:18:29.064431'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2024-07-12 10:18:29.074328'),
(13, 'auth', '0008_alter_user_username_max_length', '2024-07-12 10:18:29.161893'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2024-07-12 10:18:29.251376'),
(15, 'auth', '0010_alter_group_name_max_length', '2024-07-12 10:18:29.278882'),
(16, 'auth', '0011_update_proxy_permissions', '2024-07-12 10:18:29.290183'),
(17, 'auth', '0012_alter_user_first_name_max_length', '2024-07-12 10:18:29.377510'),
(18, 'resecurityapp', '0001_initial', '2024-07-12 10:18:31.371735'),
(19, 'resecurityapp', '0002_alter_staff_role_alter_requirement_status_and_more', '2024-07-12 10:18:32.316594'),
(20, 'resecurityapp', '0003_partner_state', '2024-07-12 10:18:32.357412'),
(21, 'resecurityapp', '0004_partner_designation', '2024-07-12 10:18:32.391048'),
(22, 'resecurityapp', '0005_partner_phone_number', '2024-07-12 10:18:32.427367'),
(23, 'sessions', '0001_initial', '2024-07-12 10:18:32.484881'),
(24, 'resecurityapp', '0006_alter_transaction_remark', '2024-07-18 03:20:23.990423'),
(25, 'resecurityapp', '0007_alter_contact_email', '2024-07-18 04:23:58.649521');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('6arfh03oq8a4f9vyai3i81y9f6gjtwo7', 'eyJmdWxsbmFtZSI6IkFkbWluIn0:1sSxPz:-_AP4b8Wc1kPyF2sIjHD57gmzmzKTPKNgrMYUdr9ygY', '2024-07-15 11:29:27.306255'),
('o8223nfiy3x9961sj4civ8rfod6umlcr', '.eJxVjDsOwjAQBe_iGln-JetQ0ucM1nq9xgHkSHFSIe5OIqWA9s3Me4uA21rC1ngJUxJXocXld4tIT64HSA-s91nSXNdlivJQ5EmbHOfEr9vp_h0UbGWvY_ad1UmZaCxlsIA94NApcINKWXuGTI6sitp4xxjJZ7fbiB4y696Kzxfeuzf6:1sTBn9:0QBDZ7vZV-rOXZO4xpr8d4odrmAXDcp5P3_V0tHFX_Q', '2024-07-16 02:50:19.193196'),
('o8y5k4ohxu5s038sb56kplkusaqhwbp4', 'eyJmdWxsbmFtZSI6IkFkbWluIn0:1sUN46:wDkS4azu-HRcfPV-zYqHX16GK0N3XGl-KkO4v12LhEE', '2024-07-19 09:04:42.361356'),
('p8cz3xaq8sexxc1y9xsyws2l7mio8qyn', '.eJxVjDsOwjAQBe_iGln-JetQ0ucM1nq9xgHkSHFSIe5OIqWA9s3Me4uA21rC1ngJUxJXocXld4tIT64HSA-s91nSXNdlivJQ5EmbHOfEr9vp_h0UbGWvY_ad1UmZaCxlsIA94NApcINKWXuGTI6sitp4xxjJZ7fbiB4y696Kzxfeuzf6:1sUN47:MFZre8_8u4tPVxJg4aDbmonBi-Ot9-9yPL12vnlQV_c', '2024-07-19 09:04:43.821454'),
('vwfh0jvjwa6o1gp3jgvn9yziegq182q0', 'eyJmdWxsbmFtZSI6IkFkbWluIn0:1sSE4K:dTmElS7dVYMYNawWgFvBHM7F60FRsG_5V2Qiw6DmwGk', '2024-07-13 11:04:04.272420'),
('zjwhlgmw4b2cjtqfl5i0g11bsr0o8vvv', 'eyJmdWxsbmFtZSI6IkFkbWluIn0:1sTIAF:4QfcV1JHQ8idlmdXdpN5nMIUdZVpas9tY5nWz3wBH-I', '2024-07-16 09:38:35.010028');

-- --------------------------------------------------------

--
-- Table structure for table `resecurityapp_brand`
--

CREATE TABLE `resecurityapp_brand` (
  `id` bigint NOT NULL,
  `Brand_Name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `resecurityapp_brand`
--

INSERT INTO `resecurityapp_brand` (`id`, `Brand_Name`) VALUES
(1, 'Resecurity');

-- --------------------------------------------------------

--
-- Table structure for table `resecurityapp_company`
--

CREATE TABLE `resecurityapp_company` (
  `id` bigint NOT NULL,
  `Company_Name` varchar(100) NOT NULL,
  `address` varchar(255) NOT NULL,
  `city` varchar(100) NOT NULL,
  `state` varchar(100) DEFAULT NULL,
  `country` varchar(100) NOT NULL,
  `Referral_Name` varchar(100) DEFAULT NULL,
  `Created_By` varchar(100) DEFAULT NULL,
  `Partner_Name_id` bigint DEFAULT NULL,
  `sector_id` bigint DEFAULT NULL,
  `via` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `resecurityapp_company`
--

INSERT INTO `resecurityapp_company` (`id`, `Company_Name`, `address`, `city`, `state`, `country`, `Referral_Name`, `Created_By`, `Partner_Name_id`, `sector_id`, `via`) VALUES
(1, 'Prabhu Bank', 'Babar Mahal', 'Kathmandu', 'BG', 'Nepal', 'Sachin', 'Admin', NULL, 1, 'Referral'),
(2, 'KEC', 'Mumbai', 'Mumbai', '', 'India', NULL, 'Admin', NULL, 2, 'Direct'),
(3, 'Ministry of Information Communication & Technology', 'Kathmandu', 'Kathmandu', 'Bagmati', 'Nepal', 'Undefined', 'Admin', NULL, 7, 'Referral'),
(4, 'Global IME Bank', 'Kathmandu', 'Kathmandu', 'Bagmati', 'Nepal', 'Undefined', 'Admin', NULL, 1, 'Referral'),
(6, 'Thomas Cook India Pvt. Ltd.', 'Mumbai', 'Mumbai', NULL, 'India', NULL, 'Admin', 1, 2, 'Partner'),
(7, 'Sanathan Textiles Limited', 'Mumbai', 'Mumbai', '', 'India', NULL, 'Admin', 1, 5, 'Partner'),
(8, 'EXL', 'Gurgaon', 'Gurgaon', '', 'India', NULL, 'Admin', NULL, 2, 'Direct'),
(9, 'IndiaHub - Egovernance Pvt. Ltd.', 'Delhi', 'Delhi', '', 'India', 'Undefined', 'Admin', NULL, NULL, 'Referral'),
(10, 'InfoDevelopers Pvt. Ltd.', 'Lalitpur', 'Lalitpur', '', 'Nepal', NULL, 'Admin', NULL, 4, 'Direct'),
(11, 'Institute of Chartered Accountant Nepal', 'Lalitpur', 'Lalitpur', '', 'Nepal', 'Undefined', 'Admin', NULL, 1, 'Referral'),
(12, 'People Group (Shaadi.com)', 'Mumbai', 'Mumbai', '', 'India', NULL, 'Admin', NULL, 5, 'Direct'),
(13, 'Kerala Police', 'Kerala', 'Kerala', '', 'India', NULL, 'Admin', NULL, NULL, 'Direct'),
(14, 'Institute of Cost Accountant of India', 'Delhi', 'Delhi', NULL, 'India', 'Undefined', 'Admin', NULL, 2, 'Referral'),
(15, 'ICICI Bank', 'Mumbai', 'Mumbai', '', 'India', NULL, 'Admin', NULL, 1, 'Direct'),
(16, 'Chandigarh University', 'Chandigarh', 'Chandirah', '', 'India', 'Undefined', 'Admin', NULL, 2, 'Referral'),
(17, 'Sunway College', 'Kathmandu', 'Kathmandu', '', 'India', NULL, 'Admin', NULL, 6, 'Direct'),
(18, 'Lumiverse Solutions Pvt. Ltd.', 'Nashik', 'Nashik', '', 'India', NULL, 'Admin', NULL, 5, 'Direct'),
(19, 'Bongobd.com', 'Dhaka', 'Dhaka', '', 'Bangladesh', NULL, 'Admin', NULL, 2, 'Direct'),
(20, 'Federation of Nepalese Chambers of Commerce & Industries (FNCCI)', 'Kathmandu', 'Kathmandu', NULL, 'Nepal', 'Undefined', 'Admin', NULL, 7, 'Referral'),
(21, 'Central Investigation Bureau', 'Kathmandu', 'Kathmandu', '', 'Nepal', NULL, 'Admin', NULL, 8, 'Direct'),
(22, 'New Business Age', 'Thapathali', 'Kathmandu', 'Bagmati', 'Nepal', NULL, 'Admin', NULL, 5, 'Direct'),
(23, 'Excelligent Consulting Services (P) Ltd.', 'Gurgaon', 'Gurgaon', '', 'India', NULL, 'Admin', NULL, 5, 'Direct'),
(24, 'Wonder Cement', 'Jaipur', 'Jaipur', NULL, 'India', NULL, 'Admin', 1, 5, 'Partner'),
(25, 'Cyberotect', 'Ahmedabad', 'Ahmedabad', '', 'India', NULL, 'Admin', 1, 4, 'Partner'),
(26, 'Prabhu Technology', 'Naxal', 'Kathmandu', 'Bagmati', 'Nepal', 'Undefined', 'Admin', NULL, 4, 'Referral'),
(27, 'Credit Information Bureau Nepal', 'Teendhara Marg', 'Kathmandu', 'Bagmati', 'Nepal', NULL, 'Admin', 1, 7, 'Partner'),
(28, 'NIC Asia Bank Ltd.', 'Kathmandu', 'Kathmandu', 'Bagmati', 'Nepal', NULL, 'Admin', 1, 1, 'Partner'),
(29, 'Log Us Business Systems Pvt. Ltd.', 'Bangalore', 'Bangalore', '', 'India', NULL, 'Admin', NULL, 5, 'Direct'),
(30, 'Nabil Bank', 'Kathmandu', 'Kathmandu', 'Bagmati', 'Nepal', NULL, 'Admin', 1, 1, 'Partner'),
(31, 'All India Council for Technical Education (AICTE)', 'Delhi', 'Delhi', '', 'India', NULL, 'Admin', 1, 7, 'Partner'),
(32, 'Yantra Solutions', 'Sanepa Heights', 'Kathmandu', 'Bagmati', 'Nepal', NULL, 'Admin', NULL, 4, 'Direct'),
(33, 'Kimerlite Commerce', 'Kathmandu', 'Kathmandu', 'Bagmati', 'Nepal', NULL, 'Admin', NULL, 5, 'Direct'),
(34, 'NDTV', 'Noida', 'Noida', NULL, 'India', NULL, 'Admin', 1, 5, 'Partner'),
(35, 'FICCI', 'Delhi', 'Delhi', '', 'India', NULL, 'Admin', NULL, 5, 'Direct'),
(36, 'Uflex Limited', 'Noida', 'Noida', '', 'India', NULL, 'Admin', 1, 5, 'Partner'),
(37, 'DSCI', 'Noida', 'Noida', '', 'India', NULL, 'Admin', NULL, 8, 'Direct'),
(38, 'Bajan Allianz Life Insurance Co. Ltd.', 'Delhi', 'Delhi', '', 'India', NULL, 'Admin', 1, 9, 'Partner'),
(39, 'Indian Center for Policy Research & Development ', 'Dharma Marg, Chanakyapuri', 'Delhi', '', 'India', NULL, 'Admin', 1, 10, 'Partner'),
(40, 'Kurukshetra University', 'Kurekshetra', 'Kurekshetra', '', 'India', NULL, 'Admin', 1, 6, 'Partner'),
(41, 'Terra Eagle', 'Bangalore', 'Bangalore', '', 'India', NULL, 'Admin', NULL, 8, 'Direct'),
(42, 'Fidrox', 'Bangalore', 'Bangalore', '', 'India', NULL, 'Admin', NULL, 8, 'Direct'),
(43, 'Kumari Bank Limited', 'Kathmandu', 'Kathmandu', 'Bagmati', 'Nepal', NULL, 'Admin', NULL, 1, 'Direct');

-- --------------------------------------------------------

--
-- Table structure for table `resecurityapp_contact`
--

CREATE TABLE `resecurityapp_contact` (
  `id` bigint NOT NULL,
  `Contact_Name` varchar(100) NOT NULL,
  `designation` varchar(100) NOT NULL,
  `email` varchar(254) NOT NULL,
  `Phone_Number` varchar(20) NOT NULL,
  `company_id` bigint NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `resecurityapp_contact`
--

INSERT INTO `resecurityapp_contact` (`id`, `Contact_Name`, `designation`, `email`, `Phone_Number`, `company_id`) VALUES
(1, 'Suresh', 'Admin Officer', 'suresh@prabhubank.com', '+977 9851041652', 1),
(2, 'Predipta', 'Undefined', 'patrop09@kecrpg.com', '+91 Undefined', 2),
(5, 'Anil Dutta', 'Undefined', 'anil.dutta@nepal.gov.np', '+977 Undefined', 3),
(6, 'Suman Pokhrel', 'Undefined', 'suman.pokhrel@gibl.com.np', '+977 Undefined', 4),
(7, 'Anil Joshi', 'Undefined', 'anil.joshi@gibl.com.np', '+977 Undefined', 4),
(9, 'Vikram Jethe Rajeshwari', 'Undefined', 'vikram.jethe@thomascook.in', '+91 Undefined', 6),
(10, 'Sushant Pawar', 'Undefined', 'sushant.pawar@63sats.com', '+91 Undefined', 7),
(11, 'Ritesh Kumar', 'Undefined', 'ritesh.kumar@exlservice.com', '+91 Undefined', 8),
(12, 'Mipandeep Singh', 'Undefined', 'mipaandeep.singh@indiahub.com', '+91 Undefined', 9),
(13, 'Umesh Raghubanshi', 'Undefined', 'umesh@infodev.com.np', '+977 Undefined', 10),
(14, 'Sujan Kafle', 'Undefined', 'sujan.kafle@ican.org.np', '+977 Undefined', 11),
(15, 'Rohit Singh', 'Undefined', 'rohit.si@peopleinteractive.in', '+91 Undefined', 12),
(16, 'Suresh V', 'Undefined', 'suresh188444.pol@kerala.gov.in', '+91 Undefined', 13),
(17, 'Ashwini Dawadi', 'Undefined', 'president@icmai.in', '+91 Undefined', 14),
(18, 'Javed P Qureshi', 'Undefined', 'javed.p@iciciban.com', '+91 Undefined', 15),
(19, 'Savin Sam', 'Undefined', 'savin.sam@cyberspace.net', '+91 Undefined', 16),
(20, 'Khushal Regmi', 'Undefined', 'khushal@sunway.edu.np', '+91 Undefined', 17),
(21, 'Amar Thakare', 'Undefined', 'amar.thakare@lumiversesolutions.com', '+91 Undefined', 18),
(22, 'Pravin Raundal', 'Undefined', 'pravin.raundal@lumiversesolutions.com', '+91 Undefined', 18),
(23, 'Ahad Bhai', 'Undefined', 'ahad@bongobd.com', '+880 Undefined', 19),
(24, 'Manoj Poudel', 'Central Committee Member', 'manoj@aadhyanta.com', '+977 Undefined', 20),
(25, 'Shyam Gyanwali', 'AIG', 'smgyanwali@yahoo.com', '+977 Undefined', 21),
(26, 'Madan Lamsal', 'CEO', 'madanlamshal@gmail.com', '+977 Undefined', 22),
(27, 'Jiban Jena', 'Undefined', 'jiban.jena@excelligent.co.in', '+91 Undefined', 23),
(29, 'Amar Rathod', 'Undefined', 'amar@tete92.com', '+91 Undefined', 24),
(30, 'Falgun Rathod', 'Undefined', 'info@cyberoctet.com', '+91 Undefined', 25),
(31, 'Bikky Shahi', 'Undefined', 'bikky@prabhupay.com', '+977 Undefined', 26),
(32, 'Mona', 'Undefined', 'mona.nyachhyon@monaltech.com', '+977 Undefined', 27),
(33, 'Narendra Mainali', 'Undefined', 'narendra.mainali@nicasiabank.com', '+977 Undefined', 28),
(34, 'Prashanth', 'Undefined', 'prashanth@logusims.com', '+91 Undefined', 29),
(35, 'Prabesh Poudel', 'Undefined', 'prabesh.poudel@nabilbank.com', '+977 Undefined', 30),
(37, 'Mipandeep Singh', 'Undefined', 'mipaandeep.singh@indiahub.com', '+91 Undefined', 31),
(38, 'Prasun Thapa', 'Undefined', 'prasun@yantra.com.np', '+977 Undefined', 32),
(39, 'Sachin Karmacharya', 'Undefined', 'commerce.kimerlite@gmail.com', '+977 Undefined', 33),
(40, 'Jaskirat Singh Bedi', 'Undefined', 'jaskirats@ndtv.com', '+91 Undefined', 34),
(41, 'Sarika Gulyani', 'Undefined', 'sarika.gulyani@ficci.com', '+91 Undefined', 35),
(42, 'Vipin Kumar', 'Undefined', 'noemail@example.com', '+91 Undefined', 36),
(43, 'Atul Kumar', 'Undefined', 'atul.kumar@dsci.in', '+91 Undefined', 37),
(44, 'Dharmendra Sengar', 'Undefined', 'dharmendra.sengar@bajajallianz.co.in', '+91 Undefined', 38),
(45, 'Rajiv Ranjan Singh', 'Undefined', 'secretarialt@icprd.org.in', '+91 Undefined', 39),
(46, 'Pankaj', 'Undefined', 'pankaj@kuk.ac.in', '+91 Undefined', 40),
(47, 'Amit Singh', 'Undefined', 'amit.singh@terraeagle.com', '+91 Undefined', 41),
(48, 'Madan Kumar', 'Undefined', 'madan.raj@fidrox.com', '+91 Undefined', 42),
(49, 'Suraj Dhungel', 'Undefined', 'suraj.dhungel@kumaribank.com', '+977 Undefined', 43);

-- --------------------------------------------------------

--
-- Table structure for table `resecurityapp_partner`
--

CREATE TABLE `resecurityapp_partner` (
  `id` bigint NOT NULL,
  `Partner_Name` varchar(100) NOT NULL,
  `address` varchar(255) NOT NULL,
  `city` varchar(100) NOT NULL,
  `country` varchar(100) NOT NULL,
  `Contact_Person` varchar(100) NOT NULL,
  `email` varchar(254) NOT NULL,
  `state` varchar(100) DEFAULT NULL,
  `designation` varchar(100) DEFAULT NULL,
  `Phone_Number` varchar(20) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `resecurityapp_partner`
--

INSERT INTO `resecurityapp_partner` (`id`, `Partner_Name`, `address`, `city`, `country`, `Contact_Person`, `email`, `state`, `designation`, `Phone_Number`) VALUES
(1, 'Partner Undefined', 'Undefined', 'Undefined', 'Undefined', 'Undefined', 'undefined@gmail.com', NULL, 'Undefined', 'Undefined');

-- --------------------------------------------------------

--
-- Table structure for table `resecurityapp_requirement`
--

CREATE TABLE `resecurityapp_requirement` (
  `id` bigint NOT NULL,
  `Requirement_Type` varchar(100) NOT NULL,
  `Product_Name` varchar(100) DEFAULT NULL,
  `Requirement_Description` longtext NOT NULL,
  `currency` varchar(100) DEFAULT NULL,
  `price` varchar(100) DEFAULT NULL,
  `Contact_Name_id` bigint DEFAULT NULL,
  `brand_id` bigint DEFAULT NULL,
  `company_id` bigint NOT NULL,
  `service_id` bigint DEFAULT NULL,
  `status` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `resecurityapp_requirement`
--

INSERT INTO `resecurityapp_requirement` (`id`, `Requirement_Type`, `Product_Name`, `Requirement_Description`, `currency`, `price`, `Contact_Name_id`, `brand_id`, `company_id`, `service_id`, `status`) VALUES
(1, 'Product', 'Risk', 'Dark Web Monitoring', 'NPR', '997000', 1, 1, 1, NULL, 'Pipeline'),
(2, 'Product', 'Risk', 'Dark Web Monitoring', 'USD', '8000', 2, 1, 2, NULL, 'Pipeline'),
(3, 'Product', 'Risk', 'Dark Web Monitoring', 'USD', '7000', 7, 1, 4, NULL, 'Pipeline'),
(4, 'Product', 'Risk', 'Dark Web Monitoring', 'USD', '8200; 8900 (Revised)', 9, 1, 6, NULL, 'Pipeline'),
(5, 'Product', 'Risk', 'Dark Web Monitoring', 'USD', '6000', 10, 1, 7, NULL, 'Pipeline'),
(6, 'Product', 'Risk', 'Dark Web Monitoring', 'USD', 'Not discussed', 11, 1, 8, NULL, 'Initiated'),
(7, 'Product', 'Risk/IDP', 'Risk/IDP', 'USD', 'Not discussed', 12, 1, 9, NULL, 'Initiated'),
(8, 'Product', 'Risk/IDP', 'Risk/IDP', 'NPR', 'Not discussed', 13, 1, 10, NULL, 'Initiated'),
(9, 'Product', 'Risk', 'Risk', 'NPR', 'Not discussed', 14, 1, 11, NULL, 'Initiated'),
(10, 'Product', 'Risk', 'Risk', 'INR', 'Not discussed', 15, 1, 12, NULL, 'Pipeline'),
(11, 'Product', 'Context/Risk', 'Context/Risk', 'INR', 'Tender', 16, 1, 13, NULL, 'Pipeline'),
(12, 'Product', 'Risk/IDP', 'Risk/IDP', 'INR', 'Per CA', 17, 1, 14, NULL, 'Initiated'),
(13, 'Product', 'Risk', 'Risk', 'USD', '10000', 18, 1, 15, NULL, 'Pipeline'),
(14, 'Product', 'Context/Risk', 'Context/Risk', 'USD', '228000', 19, 1, 16, NULL, 'No Response'),
(15, 'Product', 'IDP/One Time Risk Report', 'IDP/One Time Risk Report', 'USD', '7700', 20, 1, 17, NULL, 'Initiated'),
(16, 'Service', NULL, 'Risk Report', 'USD', '2500', 21, NULL, 18, 1, 'Pipeline'),
(17, 'Product', 'Risk', 'Risk', 'USD', 'After Response', 23, 1, 19, NULL, 'Initiated'),
(18, 'Product', 'Context/Risk Investigation Services', 'Context/Risk Investigation Services', 'NPR', 'Not discussed', 25, 1, 21, NULL, 'Initiated'),
(19, 'Product', 'Risk', 'Risk', 'USD', '3000', 26, 1, 22, NULL, 'Initiated'),
(20, 'Product', 'Risk/Services', 'Risk/Services', 'INR', 'Not discussed', 27, 1, 23, NULL, 'Initiated'),
(21, 'Product', 'Risk', 'Risk', 'USD', '6000', 29, 1, 24, NULL, 'Initiated'),
(22, 'Product', 'Risk', 'Risk', 'USD', '5000', 30, 1, 25, NULL, 'Initiated'),
(23, 'Product', 'Risk', 'Risk', 'USD', '3500', 31, 1, 26, NULL, 'Pipeline'),
(24, 'Product', 'Risk', 'Risk', 'USD', '4500', 32, 1, 27, NULL, 'Initiated'),
(25, 'Product', 'Risk', 'Risk', 'USD', '6000', 33, 1, 28, NULL, 'Pipeline'),
(26, 'Product', 'Risk', 'Risk', 'USD', '5000', 34, 1, 29, NULL, 'Pipeline'),
(27, 'Product', 'Risk', 'Risk', 'USD', '5500', 35, 1, 30, NULL, 'Pipeline'),
(28, 'Product', 'Risk', 'Risk', 'USD', '8500', 12, 1, 31, NULL, 'Initiated'),
(29, 'Product', 'Risk', 'Risk', 'NPR', 'Not discussed', 38, 1, 32, NULL, 'Pipeline'),
(30, 'Product', 'Risk', 'Risk', 'NPR', 'Not discussed', 39, 1, 33, NULL, 'Initiated'),
(31, 'Product', 'Risk', 'Risk', 'USD', '8000', 40, 1, 34, NULL, 'Initiated'),
(32, 'Service', NULL, 'MoU', 'INR', 'Not discussed', 41, NULL, 35, 2, 'Initiated'),
(33, 'Product', 'Risk', 'Risk', 'USD', '7000', 42, 1, 36, NULL, 'Initiated'),
(34, 'Service', NULL, 'MoU', 'INR', 'Not discussed', 43, NULL, 37, 2, 'Initiated'),
(35, 'Product', 'Risk', 'Risk', 'USD', '6000', 44, 1, 38, NULL, 'Initiated'),
(36, 'Service', NULL, 'MoU', 'INR', 'Not discussed', 46, NULL, 40, 2, 'Initiated'),
(37, 'Product', 'Risk', 'Risk', 'INR', 'Not discussed', 47, 1, 41, NULL, 'Pipeline'),
(38, 'Service', NULL, 'CTI', 'INR', 'Not discussed', 48, NULL, 42, 4, 'Initiated'),
(39, 'Product', 'Risk', 'Risk', 'NPR', 'Not discussed', 49, 1, 43, NULL, 'Initiated'),
(40, 'Product', 'Risk', 'Risk', 'USD', '6000', 5, 1, 3, NULL, 'Initiated'),
(41, 'Product', 'Risk', 'Risk', 'USD', '4500', 45, 1, 39, NULL, 'Initiated');

-- --------------------------------------------------------

--
-- Table structure for table `resecurityapp_sector`
--

CREATE TABLE `resecurityapp_sector` (
  `id` bigint NOT NULL,
  `Sector_Name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `resecurityapp_sector`
--

INSERT INTO `resecurityapp_sector` (`id`, `Sector_Name`) VALUES
(1, 'Banking'),
(5, 'Business'),
(6, 'Education'),
(7, 'Government'),
(4, 'IT'),
(9, 'Life Insurance'),
(10, 'Policy'),
(8, 'Security'),
(2, 'Undefined');

-- --------------------------------------------------------

--
-- Table structure for table `resecurityapp_service`
--

CREATE TABLE `resecurityapp_service` (
  `id` bigint NOT NULL,
  `Service_Name` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `resecurityapp_service`
--

INSERT INTO `resecurityapp_service` (`id`, `Service_Name`) VALUES
(3, 'Collaboration'),
(4, 'CTI'),
(2, 'MoU'),
(1, 'Risk Report');

-- --------------------------------------------------------

--
-- Table structure for table `resecurityapp_staff`
--

CREATE TABLE `resecurityapp_staff` (
  `id` bigint NOT NULL,
  `Full_Name` varchar(100) NOT NULL,
  `email` varchar(254) NOT NULL,
  `password` varchar(250) NOT NULL,
  `role` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `resecurityapp_staff`
--

INSERT INTO `resecurityapp_staff` (`id`, `Full_Name`, `email`, `password`, `role`) VALUES
(1, 'Admin', 'admin@gmail.com', 'pbkdf2_sha256$720000$GVVAW23YlcGbX4kSias7Zg$mZpGk7jJ6rzrxOT7IP9iT+1yUtvMDrZ5NgL7wHNSPWI=', 'Admin');

-- --------------------------------------------------------

--
-- Table structure for table `resecurityapp_transaction`
--

CREATE TABLE `resecurityapp_transaction` (
  `id` bigint NOT NULL,
  `date` date NOT NULL,
  `Requirement_Type` varchar(100) NOT NULL,
  `Product_Name` varchar(100) DEFAULT NULL,
  `action` longtext NOT NULL,
  `remark` longtext NOT NULL,
  `Created_By` varchar(100) DEFAULT NULL,
  `Contact_Name_id` bigint DEFAULT NULL,
  `brand_id` bigint DEFAULT NULL,
  `company_id` bigint NOT NULL,
  `service_id` bigint DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;

--
-- Dumping data for table `resecurityapp_transaction`
--

INSERT INTO `resecurityapp_transaction` (`id`, `date`, `Requirement_Type`, `Product_Name`, `action`, `remark`, `Created_By`, `Contact_Name_id`, `brand_id`, `company_id`, `service_id`) VALUES
(1, '2024-07-10', 'Product', 'Risk', 'Bid Submitted', 'Bid Opening will be on 11th July', 'Admin', 1, 1, 1, NULL),
(2, '2024-07-11', 'Product', 'Risk', 'Present in Bid Opening meeting', 'They will inform us after a week', 'Admin', 1, 1, 1, NULL),
(3, '2024-05-02', 'Product', 'Risk', 'Sent mail to remind for PO in May', 'Decision Pending', 'Admin', 2, 1, 2, NULL),
(4, '2024-05-14', 'Product', 'Risk', 'Follow up mail for the same', '', 'Admin', 2, 1, 2, NULL),
(5, '2024-05-21', 'Product', 'Risk', 'Pinged in WhatsApp; no response', '', 'Admin', 2, 1, 2, NULL),
(6, '2024-05-25', 'Product', 'Risk', 'Pinged again, received message that they will call soon', '', 'Admin', 2, 1, 2, NULL),
(7, '2024-06-05', 'Product', 'Risk', 'Got WhatsApp message that they will call next week', '', 'Admin', 2, 1, 2, NULL),
(8, '2024-06-25', 'Product', 'Risk', 'Called in his direct mobile from Bangalore; he said he\'ll do, need to follow up again', '', 'Admin', 2, 1, 2, NULL),
(9, '2024-05-07', 'Product', 'Risk', 'Called and reminded to provide date', 'In progress', 'Admin', 7, 1, 4, NULL),
(10, '2024-05-13', 'Product', 'Risk', 'Reminded in WhatsApp message', '', 'Admin', 7, 1, 4, NULL),
(11, '2024-05-20', 'Product', 'Risk', 'Got response; ISO is sick and assured to provide date for May 23', '', 'Admin', 7, 1, 4, NULL),
(12, '2024-05-27', 'Product', 'Risk', 'No response on two times call', '', 'Admin', 7, 1, 4, NULL),
(13, '2024-05-29', 'Product', 'Risk', 'Received call from ISO; they are planning to have demo on June 3', 'In progress', 'Staff', 7, 1, 4, NULL),
(14, '2024-06-05', 'Product', 'Risk', 'Their team got accident and no postponed', '', 'Admin', 7, 1, 4, NULL),
(15, '2024-06-30', 'Product', 'Risk', 'Called that after July 17 Nepali Financial Year', '', 'Admin', 7, 1, 4, NULL),
(16, '2024-04-03', 'Product', 'Risk', 'Demo provided', '', 'Admin', 9, 1, 6, NULL),
(17, '2024-04-04', 'Product', 'Risk', 'Proposal sent', '', 'Admin', 9, 1, 6, NULL),
(18, '2024-04-08', 'Product', 'Risk', 'Asked feedback of proposal; received feedback', '', 'Admin', 9, 1, 6, NULL),
(19, '2024-04-16', 'Product', 'Risk', 'They want 15 domains in 9 companies; asked them to quote price maximum of USD 11,500', '', 'Admin', 9, 1, 6, NULL),
(20, '2024-04-22', 'Product', 'Risk', 'Partner email us; they are waiting for client response', '', 'Admin', 9, 1, 6, NULL),
(21, '2024-04-30', 'Product', 'Risk', 'Reminder mail sent to partner', '', 'Admin', 9, 1, 6, NULL),
(22, '2024-04-30', 'Product', 'Risk', 'Partner sent mail and asked revised price after adding 5 more domains', '', 'Admin', 9, 1, 6, NULL),
(23, '2024-05-01', 'Product', 'Risk', 'We proposed for 3 years, USD 24K and for one year 8900/- after adding 5 more domains', '', 'Admin', 9, 1, 6, NULL),
(24, '2024-05-07', 'Product', 'Risk', 'Received queries with revive cost for 5 domains only', '', 'Admin', 9, 1, 6, NULL),
(25, '2024-05-08', 'Product', 'Risk', 'Revive Cost with queries replied', '', 'Admin', 9, 1, 6, NULL),
(26, '2024-05-10', 'Product', 'Risk', 'Chat with partner\'s account manager, she is sick, told she will contact after she recovered', '', 'Admin', 9, 1, 6, NULL),
(27, '2024-05-22', 'Product', 'Risk', 'Proposed for another demo with client on 29th May', '', 'Admin', 9, 1, 6, NULL),
(28, '2024-05-29', 'Product', 'Risk', 'Demo provided, Mark internet was poor, however, we have shown demo clearly. They have asked to show how many they have social media account thru our platform, we had replied that client can monitor by adding social media account in digital foot print  where it\'s exposed on the Internet, it allows to initiate monitoring on social networks for brand protection and social media analysis. If your brand is in any social media platform like twitter, facebook etc it will show and can be analysis further and also possible to take down.', '', 'Admin', 9, 1, 6, NULL),
(29, '2024-04-08', 'Product', 'Risk', 'Asked about the status', 'After demo, partner will send MoU', 'Admin', 10, 1, 7, NULL),
(30, '2024-04-09', 'Product', 'Risk', 'Received status; they are meeting on April 15 and update us', '', 'Admin', 10, 1, 7, NULL),
(31, '2024-04-22', 'Product', 'Risk', 'Sent mail to update status; received mail to confirm the price for 3 years as INR 5,40,000/- i.e around USD 6477/- per year; we confirmed it', '', 'Admin', 10, 1, 7, NULL),
(32, '2024-04-30', 'Product', 'Risk', 'Talked with partner, they are following up with client', '', 'Admin', 10, 1, 7, NULL),
(33, '2024-04-02', 'Product', 'Risk', 'Got email, and wants to meet in person', 'While visiting India, we\'ll meet him', 'Admin', 11, 1, 8, NULL),
(34, '2024-05-16', 'Product', 'Risk/IDP', 'Had a meeting with their team; noted all their queries', '', 'Admin', 12, 1, 9, NULL),
(35, '2024-05-18', 'Product', 'Risk/IDP', 'Replied their queries and sent EPP datasheet', '', 'Admin', 12, 1, 9, NULL),
(36, '2024-05-20', 'Product', 'Risk/IDP', 'Asked cost of platform in mail; replied that depends on CTI assets and scope of work, sent CTI asset form', 'Waiting for signed NDA', 'Admin', 12, 1, 9, NULL),
(37, '2024-05-01', 'Product', 'Risk/IDP', 'Received mail stating that they are busy on other matters will inform us later on; most probably after July 15th', 'Demo for 3rd April;\r\nThey provided the Core Banking Software to 3 A Class and all B class Banks in Nepal;\r\nWaiting for their mail for further plan', 'Admin', 13, 1, 10, NULL),
(38, '2024-04-05', 'Product', 'Risk', 'In-person meeting', '', 'Admin', 14, 1, 11, NULL),
(39, '2024-04-07', 'Product', 'Risk', 'Request letter sent for MoU', '', 'Admin', 14, 1, 11, NULL),
(40, '2024-04-22', 'Product', 'Risk', 'Reminder mail sent', '', 'Admin', 14, 1, 11, NULL),
(41, '2024-04-29', 'Product', 'Risk', 'Got message that their council meeting discussing this', '', 'Admin', 14, 1, 11, NULL),
(42, '2024-05-05', 'Product', 'Risk', 'Called them; they are busy on May month for their official election so suggested to contact on June', '', 'Admin', 14, 1, 11, NULL),
(43, '2024-06-11', 'Product', 'Risk', 'Said they are trying and will intimate us', 'Waiting for response', 'Admin', 14, 1, 11, NULL),
(44, '2024-05-02', 'Product', 'Risk', 'Followed up in WhatsApp; no response', '', 'Admin', 15, 1, 12, NULL),
(45, '2024-05-07', 'Product', 'Risk', 'Followed up in email; no response', '', 'Admin', 15, 1, 12, NULL),
(46, '2024-05-07', 'Product', 'Risk', 'Followed up in WhatsApp; no response', '', 'Admin', 15, 1, 12, NULL),
(47, '2024-05-13', 'Product', 'Risk', 'Followed up in WhatsApp; no response', '', 'Admin', 15, 1, 12, NULL),
(48, '2024-05-14', 'Product', 'Risk', 'Followed up in WhatsApp; no response', '', 'Admin', 15, 1, 12, NULL),
(49, '2024-05-21', 'Product', 'Risk', 'Followed up in WhatsApp; got reply, he is busy in some task and will connect', '', 'Admin', 15, 1, 12, NULL),
(50, '2024-05-25', 'Product', 'Risk', 'Followed up again; no response', '', 'Admin', 15, 1, 12, NULL),
(51, '2024-06-03', 'Product', 'Risk', 'Got response that they will contact in 2nd week of June', 'Reviewing commercial', 'Admin', 15, 1, 12, NULL),
(52, '2024-04-23', 'Product', 'Context/Risk', 'Mr. Kiran RS entered in the discussion by sending message in WhatsApp', '', 'Admin', 16, 1, 13, NULL),
(53, '2024-05-09', 'Product', 'Context/Risk', 'Pinged in WhatsApp; no response', '', 'Admin', 16, 1, 13, NULL),
(54, '2024-05-13', 'Product', 'Context/Risk', 'Pinged again, received message; he is busy in class', '', 'Admin', 16, 1, 13, NULL),
(55, '2024-05-20', 'Product', 'Context/Risk', 'Agreed to Join in meeting for 21st May', '', 'Admin', 16, 1, 13, NULL),
(56, '2024-05-21', 'Product', 'Context/Risk', 'Demo provided; asked sample report in WhatsApp and suggested to have another round of meeting with seniors, and he will schedule it', '', 'Admin', 16, 1, 13, NULL),
(57, '2024-05-22', 'Product', 'Context/Risk', 'Provided sample report in email and same day received acknowledge and suggested Kiran will shaJure for further processing', '', 'Admin', 16, 1, 13, NULL),
(58, '2024-05-25', 'Product', 'Context/Risk', 'Pinged to ask date for the meeting with seniors in WhatsApp; no response', '', 'Admin', 16, 1, 13, NULL),
(59, '2024-05-26', 'Product', 'Context/Risk', 'Again pinged and followed up no response', '', 'Admin', 16, 1, 13, NULL),
(60, '2024-05-29', 'Product', 'Context/Risk', 'Followed up in WhatsApp', '', 'Admin', 16, 1, 13, NULL),
(61, '2024-06-14', 'Product', 'Context/Risk', 'Spoke on call, he said he is not getting time of seniors; once he gets he will inform us', '', 'Admin', 16, 1, 13, NULL),
(62, '2024-06-26', 'Product', 'Context/Risk', 'Called in Kiran number, saying that he is trying to arrange the meeting with higher officers', 'In progress', 'Admin', 16, 1, 13, NULL),
(63, '2024-04-18', 'Product', 'Risk/IDP', 'Received WhatsApp message to resend the proposal and sent immediately', '', 'Admin', 17, 1, 14, NULL),
(64, '2024-05-22', 'Product', 'Risk/IDP', 'Asked about update in WhatsApp; no response', 'Decision pending', 'Admin', 17, 1, 14, NULL),
(65, '2024-03-21', 'Product', 'Risk', 'Presentation with CISO; Rescheduled to April 3', '', 'Admin', 18, 1, 15, NULL),
(66, '2024-04-03', 'Product', 'Risk', 'Presentation was postponed', '', 'Admin', 18, 1, 15, NULL),
(67, '2024-04-06', 'Product', 'Risk', 'Got a call from Javed that new meeting has been scheduled for 18th April, they are sending mail after finalizing the time', '', 'Admin', 18, 1, 15, NULL),
(68, '2024-04-18', 'Product', 'Risk', 'Finally we did the presentation', '', 'Admin', 18, 1, 15, NULL),
(69, '2024-04-19', 'Product', 'Risk', 'Called Javed and got feedback; he was telling me that company presence in India will be an added advantage. They don\'t deal with partner', '', 'Admin', 18, 1, 15, NULL),
(70, '2024-04-22', 'Product', 'Risk', 'Mail sent with thanks', '', 'Admin', 18, 1, 15, NULL),
(71, '2024-04-24', 'Product', 'Risk', 'Called and asked about Deepfake Identification and API Security, replied in WhatsApp', '', 'Admin', 18, 1, 15, NULL),
(72, '2024-05-24', 'Product', 'Risk', 'Set up demo by them for Fraud Invention for 31st May', '', 'Admin', 18, 1, 15, NULL),
(73, '2024-05-30', 'Product', 'Risk', 'They have postponed it and called me that they will be rescheduling it after first week of June', '', 'Admin', 18, 1, 15, NULL),
(74, '2024-05-21', 'Product', 'Risk', 'They sent mail for Deep Fake Identification demo', '', 'Admin', 18, 1, 15, NULL),
(75, '2024-05-23', 'Product', 'Risk', 'We replied and asked any specific case, but no reply', 'They are trying to get knowledge from us', 'Admin', 18, 1, 15, NULL),
(76, '2024-02-19', 'Product', 'Context/Risk', 'Proposal sent;\r\nGood Response, they assured at least some part of the project will be given to us. We will come to know by the end of this month;\r\nWe called them and now they are saying it will be on process in April only', 'No response', 'Admin', 19, 1, 16, NULL),
(77, '2024-04-08', 'Product', 'Context/Risk', 'Mail send to Savin for update; no update and no response', '', 'Admin', 19, 1, 16, NULL),
(78, '2024-07-14', 'Product', 'IDP/One Time Risk Report', 'For November intake only', 'Waiting for demo date', 'Admin', 20, 1, 17, NULL),
(79, '2024-03-20', 'Service', NULL, 'Request received for cooperative Bank about Risk report for INR 10K', '', 'Admin', 21, NULL, 18, 1),
(80, '2024-03-21', 'Service', NULL, 'Proposal Sent', '', 'Admin', 21, NULL, 18, 1),
(81, '2024-03-21', 'Service', NULL, 'Received signed proposal', '', 'Admin', 21, NULL, 18, 1),
(82, '2024-03-26', 'Service', NULL, 'Request to have some deals before 31st March', '', 'Admin', 21, NULL, 18, 1),
(83, '2024-04-08', 'Service', NULL, 'Asked for deal, said he had started seeding and will update after 3rd week of April', '', 'Admin', 21, NULL, 18, 1),
(84, '2024-04-22', 'Service', NULL, 'Got WhatsApp message; they have started seeding details to their client', '', 'Admin', 21, NULL, 18, 1),
(85, '2024-04-30', 'Service', NULL, 'Asked for update in WhatsApp; no leads till today', '', 'Admin', 21, NULL, 18, 1),
(86, '2024-05-14', 'Service', NULL, 'Pinged to share the lead', 'Waiting for response', 'Admin', 21, NULL, 18, 1),
(87, '2024-07-15', 'Product', 'Risk', 'No response', 'Waiting for response', 'Admin', 23, 1, 19, NULL),
(88, '2024-07-15', 'Product', 'Context/Risk Investigation Services', 'No response', 'Waiting for response', 'Admin', 25, 1, 21, NULL),
(89, '2024-03-31', 'Product', 'Risk', 'Had a one-to-one meeting and sent the proposal', '', 'Admin', 26, 1, 22, NULL),
(90, '2024-04-08', 'Product', 'Risk', 'Had a person meeting; they said they will revert back', '', 'Admin', 26, 1, 22, NULL),
(91, '2024-04-15', 'Product', 'Risk', 'Had a meeting in person; they will close deal by the end of April', '', 'Admin', 26, 1, 22, NULL),
(92, '2024-04-22', 'Product', 'Risk', 'Meeting in person and shown demo for their team too', '', 'Admin', 26, 1, 22, NULL),
(93, '2024-04-29', 'Product', 'Risk', 'Pushed to release PO with their budget', '', 'Admin', 26, 1, 22, NULL),
(94, '2024-05-07', 'Product', 'Risk', 'Suggest them to be a referral in physical meeting; he accepted and call meeting for 15th May', '', 'Admin', 26, 1, 22, NULL),
(95, '2024-05-15', 'Product', 'Risk', 'They are changing server after that they will think; need to contact on June 2', '', 'Admin', 26, 1, 22, NULL),
(96, '2024-06-02', 'Product', 'Risk', 'Said they have no budget now', '', 'Admin', 26, 1, 22, NULL),
(97, '2024-06-30', 'Product', 'Risk', 'Further details/meetings after July', 'Waiting for response', 'Admin', 26, 1, 22, NULL),
(98, '2024-03-08', 'Product', 'Risk/Services', 'Received mail; want to know more about our product and solutions', '', 'Admin', 27, 1, 23, NULL),
(99, '2024-03-13', 'Product', 'Risk/Services', 'Demo Provided and Shared NDA', '', 'Admin', 27, 1, 23, NULL),
(100, '2024-03-21', 'Product', 'Risk/Services', 'Received Signed NDA', '', 'Admin', 27, 1, 23, NULL),
(101, '2024-03-22', 'Product', 'Risk/Services', 'Send Reseller Agreement', '', 'Admin', 27, 1, 23, NULL),
(102, '2024-04-10', 'Product', 'Risk/Services', 'Received Singed Agreement', '', 'Admin', 27, 1, 23, NULL),
(103, '2024-04-22', 'Product', 'Risk/Services', 'Sent meeting invite for Sales Training', '', 'Admin', 27, 1, 23, NULL),
(104, '2024-04-23', 'Product', 'Risk/Services', 'Provided sales training', '', 'Admin', 27, 1, 23, NULL),
(105, '2024-04-29', 'Product', 'Risk/Services', 'WhatsApp call to clear some doubts', '', 'Admin', 27, 1, 23, NULL),
(106, '2024-05-07', 'Product', 'Risk/Services', 'Followed up ablut leads, got reply; one company responded however, no demo date provided.', '', 'Admin', 27, 1, 23, NULL),
(107, '2024-05-15', 'Product', 'Risk/Services', 'Follow up for any lead; they are saying they are trying', 'Became the Reseller Partner and now exploring with their own existing customer and new leads.', 'Admin', 27, 1, 23, NULL),
(108, '2024-04-30', 'Product', 'Risk', 'Mail sent for Demo meeting fixed for 1st May 2024', '', 'Admin', 29, 1, 24, NULL),
(109, '2024-05-01', 'Product', 'Risk', 'Demo provided', '', 'Admin', 29, 1, 24, NULL),
(110, '2024-05-06', 'Product', 'Risk', 'CTI asset, List, Sample Report, Portfolio and Datasheet provided', '', 'Admin', 29, 1, 24, NULL),
(111, '2024-05-11', 'Product', 'Risk', 'Had a WhatsApp Call told us to wait more 10 days', '', 'Admin', 29, 1, 24, NULL),
(112, '2024-05-24', 'Product', 'Risk', 'Called them found client asked to wait more one week', '', 'Admin', 29, 1, 24, NULL),
(113, '2024-06-04', 'Product', 'Risk', 'Reminder mail sent on', '', 'Admin', 29, 1, 24, NULL),
(114, '2024-06-13', 'Product', 'Risk', 'Called to partner again', 'Demo to be provided', 'Admin', 29, 1, 24, NULL),
(115, '2024-05-03', 'Product', 'Risk', 'Demo provided on behalf of Amco Bank; they attended', '', 'Admin', 30, 1, 25, NULL),
(116, '2024-05-07', 'Product', 'Risk', 'Reminder mail sent for update', '', 'Admin', 30, 1, 25, NULL),
(117, '2024-05-14', 'Product', 'Risk', 'Reminder mail sent', '', 'Admin', 30, 1, 25, NULL),
(118, '2024-05-31', 'Product', 'Risk', 'Pinged again and suggested to meet in Gandhinagar on 10th afternoon', '', 'Admin', 30, 1, 25, NULL),
(119, '2024-06-10', 'Product', 'Risk', 'Called while in Gujarat but no response', 'Demo provided and information shared', 'Admin', 30, 1, 25, NULL),
(120, '2024-05-15', 'Product', 'Risk', 'Had a meeting with Mr. Naresh Mishra who is telecom aggregator for Payment Service Providers and proposed to be referral for our solutions and we will pay 30% of the deal amount. He had agree on this', '', 'Admin', 31, 1, 26, NULL),
(121, '2024-05-16', 'Product', 'Risk', 'Asked proposal of Risk for Prabhu Technology (PrabhuPay); submitted proposal', '', 'Admin', 31, 1, 26, NULL),
(122, '2024-05-31', 'Product', 'Risk', 'Reminder sent on call and WhatsApp; said they are processing it', '', 'Admin', 31, 1, 26, NULL),
(123, '2024-06-02', 'Product', 'Risk', 'They called me and told that concern person\'s wife is in hospital so he is in leave for 10 Days', 'Under evaluation', 'Admin', 31, 1, 26, NULL),
(124, '2024-05-27', 'Product', 'Risk', 'Proposal sent via Monal Tech', '', 'Admin', 32, 1, 27, NULL),
(125, '2024-06-05', 'Product', 'Risk', 'They have put in budget, will procure in next financial year around August', 'Waiting for progress', 'Admin', 32, 1, 27, NULL),
(126, '2024-05-27', 'Product', 'Risk', 'Met ISO Narendra and reinitiated the deal thru Partner Yantra Solutions; Planning to have demo again between 2 to 7 June', '', 'Admin', 33, 1, 28, NULL),
(127, '2024-06-06', 'Product', 'Risk', 'They told on call that they will send date after June 15th', '', 'Admin', 33, 1, 28, NULL),
(128, '2024-06-19', 'Product', 'Risk', 'Called them, saying they can take decision after July 16 only (Nepal Financial year closed on July 16th)', 'Seeking demo again for new team', 'Admin', 33, 1, 28, NULL),
(129, '2024-05-29', 'Product', 'Risk', 'Shown interest to buy license', '', 'Admin', 34, 1, 29, NULL),
(130, '2024-05-29', 'Product', 'Risk', 'We quoted price of USD 3K and sent NDA and Reseller Agreement', '', 'Admin', 34, 1, 29, NULL),
(131, '2024-05-29', 'Product', 'Risk', 'Asked us for 10 domains price', '', 'Admin', 34, 1, 29, NULL),
(132, '2024-05-30', 'Product', 'Risk', 'Called him and sent proposal of USD 5K for 10 domains', '', 'Admin', 34, 1, 29, NULL),
(133, '2024-06-01', 'Product', 'Risk', 'Received acknowledge and ask their team to sign and send', '', 'Admin', 34, 1, 29, NULL),
(134, '2024-06-06', 'Product', 'Risk', 'Reminder message in WhatsApp to send signed PO', '', 'Admin', 34, 1, 29, NULL),
(135, '2024-06-25', 'Product', 'Risk', 'Asked for signed PO', '', 'Admin', 34, 1, 29, NULL),
(136, '2024-06-28', 'Product', 'Risk', 'Called while I was in Bangalore, but still not issued', '', 'Admin', 34, 1, 29, NULL),
(137, '2024-07-01', 'Product', 'Risk', 'Mail sent and given one week time', 'Confirmed by email; Signed copy need to receive.', 'Admin', 34, 1, 29, NULL),
(138, '2024-06-04', 'Product', 'Risk', 'Shared RFP to ops@', '', 'Admin', 35, 1, 30, NULL),
(139, '2024-06-06', 'Product', 'Risk', 'RFP Submitted', '', 'Admin', 35, 1, 30, NULL),
(140, '2024-06-18', 'Product', 'Risk', 'Demo provided, they have asked the customer reference and we provided of Nepal\'s Banks names', 'Waiting for their decision', 'Admin', 35, 1, 30, NULL),
(141, '2024-06-06', 'Product', 'Risk', 'Mail sent to AICTE by partner and called me and marked cc to us', '', 'Admin', 12, 1, 31, NULL),
(142, '2024-06-12', 'Product', 'Risk', 'Called him while I was in Delhi; he was out of town', 'Waiting for response', 'Admin', 12, 1, 31, NULL),
(143, '2024-06-02', 'Product', 'Risk', 'Shown interest to be reseller partner and we sent NDA', '', 'Admin', 38, 1, 32, NULL),
(144, '2024-06-03', 'Product', 'Risk', 'Received signed NDA and Reseller agreement and we also sent after signed it', '', 'Admin', 38, 1, 32, NULL),
(145, '2024-06-04', 'Product', 'Risk', 'Proposed us to discuss to provide CTI related awareness to Member of Nepal Banker Association', '', 'Admin', 38, 1, 32, NULL),
(146, '2024-06-05', 'Product', 'Risk', 'Discussed with them and now getting appointment with Jagadish Nepal (NBA) and Shreejan (NCHL) for the same', 'Appointment with NBA is waiting', 'Admin', 38, 1, 32, NULL),
(147, '2024-06-08', 'Product', 'Risk', 'Meet personally and explained about our company product and services', '', 'Admin', 39, 1, 33, NULL),
(148, '2024-06-09', 'Product', 'Risk', 'Got response in email that they will inform us the demo date and time', '', 'Admin', 39, 1, 33, NULL),
(149, '2024-06-11', 'Product', 'Risk', 'Proposed Demo date for 12th June 6:30 PM and meeting link sent', '', 'Admin', 39, 1, 33, NULL),
(150, '2024-06-12', 'Product', 'Risk', 'Demo provided, they proposed to meet on 16th June', 'Meeting on 16th June', 'Admin', 39, 1, 33, NULL),
(151, '2024-06-12', 'Product', 'Risk', 'Had a meeting with him and Kapil Sethi thru partner, good response; Demo provided; they are aligning with their digital team for another demo', '', 'Admin', 40, 1, 34, NULL),
(152, '2024-06-26', 'Product', 'Risk', 'Proposal Submitted', '', 'Admin', 40, 1, 34, NULL),
(153, '2024-06-12', 'Service', NULL, 'Had a meeting with her, presented our corporate profile. They are initially interested to have workshop with us', '', 'Admin', 41, NULL, 35, 2),
(154, '2024-06-25', 'Service', NULL, 'Reminder Mail Sent', '', 'Admin', 41, NULL, 35, 2),
(155, '2024-06-26', 'Service', NULL, 'Threat feed provided in both mail and WhatsApp', 'Need to send details', 'Admin', 41, NULL, 35, 2),
(156, '2024-06-13', 'Product', 'Risk', 'Shown the demo and corporate profile; now sending sample report, datasheet and profile', '', 'Admin', 42, 1, 36, NULL),
(157, '2024-06-26', 'Product', 'Risk', 'Proposal submitted', 'They are asking PoC', 'Admin', 42, 1, 36, NULL),
(158, '2024-06-13', 'Service', NULL, 'Had a good meeting discuss about potential collaboration, they also asked the MoU format and wants one discussion program with high level officials of their member in first phase', '', 'Admin', 43, NULL, 37, 2),
(159, '2024-06-25', 'Service', NULL, 'Reminder Mail Sent', 'Providing details to them', 'Admin', 43, NULL, 37, 2),
(160, '2024-06-14', 'Product', 'Risk', 'Had a talk along with Partner ', 'Sample report provided through partner', 'Admin', 44, 1, 38, NULL),
(161, '2024-06-14', 'Service', NULL, 'Draft MoU sent', '', 'Admin', 46, NULL, 40, 2),
(162, '2024-06-22', 'Product', 'Risk', 'Meet on Stall', '', 'Admin', 47, 1, 41, NULL),
(163, '2024-06-25', 'Product', 'Risk', 'Met in office; demo provided', '', 'Admin', 47, 1, 41, NULL),
(164, '2024-06-28', 'Product', 'Risk', 'Final Demo', 'Demo provided and information shared', 'Admin', 47, 1, 41, NULL),
(165, '2024-06-24', 'Service', NULL, 'Had a physical meeting and explore', '', 'Admin', 48, NULL, 42, 4),
(166, '2024-07-01', 'Service', NULL, 'Asked the use case for Airport', 'Infosys and Bangalore airport are their client; they need use case of Airport and arranging meeting cyber security team of Infosys', 'Admin', 48, NULL, 42, 4),
(167, '2024-06-30', 'Product', 'Risk', 'Demo provided', 'Asking PoC', 'Admin', 49, 1, 43, NULL),
(168, '2024-04-01', 'Product', 'Risk', 'Had a call, asked to send proposal; proposal sent on same day', '', 'Admin', 5, 1, 3, NULL),
(169, '2024-04-04', 'Product', 'Risk', 'Met personally and discussed. However, he said to wait until August 2024 to get the budget in new financial Year', 'Following up', 'Admin', 5, 1, 3, NULL),
(170, '2024-06-14', 'Product', 'Risk', 'Demo provided', 'They are the nodal agency for policy formulation of all Ministries', 'Admin', 45, 1, 39, NULL);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `auth_group`
--
ALTER TABLE `auth_group`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `name` (`name`);

--
-- Indexes for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  ADD KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`);

--
-- Indexes for table `auth_user`
--
ALTER TABLE `auth_user`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`);

--
-- Indexes for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  ADD KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`);

--
-- Indexes for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  ADD KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`);

--
-- Indexes for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD PRIMARY KEY (`id`),
  ADD KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  ADD KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`);

--
-- Indexes for table `django_content_type`
--
ALTER TABLE `django_content_type`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`);

--
-- Indexes for table `django_migrations`
--
ALTER TABLE `django_migrations`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `django_session`
--
ALTER TABLE `django_session`
  ADD PRIMARY KEY (`session_key`),
  ADD KEY `django_session_expire_date_a5c62663` (`expire_date`);

--
-- Indexes for table `resecurityapp_brand`
--
ALTER TABLE `resecurityapp_brand`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `Brand_Name` (`Brand_Name`);

--
-- Indexes for table `resecurityapp_company`
--
ALTER TABLE `resecurityapp_company`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `Company_Name` (`Company_Name`),
  ADD KEY `resecurityapp_compan_Partner_Name_id_483e780d_fk_resecurit` (`Partner_Name_id`),
  ADD KEY `resecurityapp_compan_sector_id_baba9116_fk_resecurit` (`sector_id`);

--
-- Indexes for table `resecurityapp_contact`
--
ALTER TABLE `resecurityapp_contact`
  ADD PRIMARY KEY (`id`),
  ADD KEY `resecurityapp_contac_company_id_e0ff2e96_fk_resecurit` (`company_id`);

--
-- Indexes for table `resecurityapp_partner`
--
ALTER TABLE `resecurityapp_partner`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `resecurityapp_requirement`
--
ALTER TABLE `resecurityapp_requirement`
  ADD PRIMARY KEY (`id`),
  ADD KEY `resecurityapp_requir_Contact_Name_id_7af6f25f_fk_resecurit` (`Contact_Name_id`),
  ADD KEY `resecurityapp_requir_brand_id_f85e6931_fk_resecurit` (`brand_id`),
  ADD KEY `resecurityapp_requir_company_id_0580bda1_fk_resecurit` (`company_id`),
  ADD KEY `resecurityapp_requir_service_id_1af8f06e_fk_resecurit` (`service_id`);

--
-- Indexes for table `resecurityapp_sector`
--
ALTER TABLE `resecurityapp_sector`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `Sector_Name` (`Sector_Name`);

--
-- Indexes for table `resecurityapp_service`
--
ALTER TABLE `resecurityapp_service`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `Service_Name` (`Service_Name`);

--
-- Indexes for table `resecurityapp_staff`
--
ALTER TABLE `resecurityapp_staff`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `email` (`email`);

--
-- Indexes for table `resecurityapp_transaction`
--
ALTER TABLE `resecurityapp_transaction`
  ADD PRIMARY KEY (`id`),
  ADD KEY `resecurityapp_transa_Contact_Name_id_8501358c_fk_resecurit` (`Contact_Name_id`),
  ADD KEY `resecurityapp_transa_brand_id_bb1d2e19_fk_resecurit` (`brand_id`),
  ADD KEY `resecurityapp_transa_company_id_10e11165_fk_resecurit` (`company_id`),
  ADD KEY `resecurityapp_transa_service_id_1e23b67d_fk_resecurit` (`service_id`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=61;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=26;

--
-- AUTO_INCREMENT for table `resecurityapp_brand`
--
ALTER TABLE `resecurityapp_brand`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `resecurityapp_company`
--
ALTER TABLE `resecurityapp_company`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=44;

--
-- AUTO_INCREMENT for table `resecurityapp_contact`
--
ALTER TABLE `resecurityapp_contact`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=50;

--
-- AUTO_INCREMENT for table `resecurityapp_partner`
--
ALTER TABLE `resecurityapp_partner`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `resecurityapp_requirement`
--
ALTER TABLE `resecurityapp_requirement`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=42;

--
-- AUTO_INCREMENT for table `resecurityapp_sector`
--
ALTER TABLE `resecurityapp_sector`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=11;

--
-- AUTO_INCREMENT for table `resecurityapp_service`
--
ALTER TABLE `resecurityapp_service`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;

--
-- AUTO_INCREMENT for table `resecurityapp_staff`
--
ALTER TABLE `resecurityapp_staff`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `resecurityapp_transaction`
--
ALTER TABLE `resecurityapp_transaction`
  MODIFY `id` bigint NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=171;

--
-- Constraints for dumped tables
--

--
-- Constraints for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`);

--
-- Constraints for table `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- Constraints for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- Constraints for table `resecurityapp_company`
--
ALTER TABLE `resecurityapp_company`
  ADD CONSTRAINT `resecurityapp_compan_Partner_Name_id_483e780d_fk_resecurit` FOREIGN KEY (`Partner_Name_id`) REFERENCES `resecurityapp_partner` (`id`),
  ADD CONSTRAINT `resecurityapp_compan_sector_id_baba9116_fk_resecurit` FOREIGN KEY (`sector_id`) REFERENCES `resecurityapp_sector` (`id`);

--
-- Constraints for table `resecurityapp_contact`
--
ALTER TABLE `resecurityapp_contact`
  ADD CONSTRAINT `resecurityapp_contac_company_id_e0ff2e96_fk_resecurit` FOREIGN KEY (`company_id`) REFERENCES `resecurityapp_company` (`id`);

--
-- Constraints for table `resecurityapp_requirement`
--
ALTER TABLE `resecurityapp_requirement`
  ADD CONSTRAINT `resecurityapp_requir_brand_id_f85e6931_fk_resecurit` FOREIGN KEY (`brand_id`) REFERENCES `resecurityapp_brand` (`id`),
  ADD CONSTRAINT `resecurityapp_requir_company_id_0580bda1_fk_resecurit` FOREIGN KEY (`company_id`) REFERENCES `resecurityapp_company` (`id`),
  ADD CONSTRAINT `resecurityapp_requir_Contact_Name_id_7af6f25f_fk_resecurit` FOREIGN KEY (`Contact_Name_id`) REFERENCES `resecurityapp_contact` (`id`),
  ADD CONSTRAINT `resecurityapp_requir_service_id_1af8f06e_fk_resecurit` FOREIGN KEY (`service_id`) REFERENCES `resecurityapp_service` (`id`);

--
-- Constraints for table `resecurityapp_transaction`
--
ALTER TABLE `resecurityapp_transaction`
  ADD CONSTRAINT `resecurityapp_transa_brand_id_bb1d2e19_fk_resecurit` FOREIGN KEY (`brand_id`) REFERENCES `resecurityapp_brand` (`id`),
  ADD CONSTRAINT `resecurityapp_transa_company_id_10e11165_fk_resecurit` FOREIGN KEY (`company_id`) REFERENCES `resecurityapp_company` (`id`),
  ADD CONSTRAINT `resecurityapp_transa_Contact_Name_id_8501358c_fk_resecurit` FOREIGN KEY (`Contact_Name_id`) REFERENCES `resecurityapp_contact` (`id`),
  ADD CONSTRAINT `resecurityapp_transa_service_id_1e23b67d_fk_resecurit` FOREIGN KEY (`service_id`) REFERENCES `resecurityapp_service` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
