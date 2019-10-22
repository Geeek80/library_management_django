-- phpMyAdmin SQL Dump
-- version 4.8.3
-- https://www.phpmyadmin.net/
--
-- Host: localhost
-- Generation Time: Oct 22, 2019 at 03:47 PM
-- Server version: 10.1.36-MariaDB
-- PHP Version: 7.2.11

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Database: `library_mgmt`
--

-- --------------------------------------------------------

--
-- Table structure for table `accountant`
--

CREATE TABLE `accountant` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL,
  `username` varchar(15) NOT NULL,
  `password` varchar(21) NOT NULL,
  `email` varchar(254) NOT NULL,
  `phone_no` varchar(13) NOT NULL,
  `resi_address` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `accountant`
--

INSERT INTO `accountant` (`id`, `name`, `username`, `password`, `email`, `phone_no`, `resi_address`) VALUES
(1, 'someone', 'someone', 'someone', 'tolaniaakash80@gmail.com', '9999999999', 'ahmedabad');

-- --------------------------------------------------------

--
-- Table structure for table `auth_group`
--

CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_group_permissions`
--

CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_permission`
--

CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can view log entry', 1, 'view_logentry'),
(5, 'Can add permission', 2, 'add_permission'),
(6, 'Can change permission', 2, 'change_permission'),
(7, 'Can delete permission', 2, 'delete_permission'),
(8, 'Can view permission', 2, 'view_permission'),
(9, 'Can add group', 3, 'add_group'),
(10, 'Can change group', 3, 'change_group'),
(11, 'Can delete group', 3, 'delete_group'),
(12, 'Can view group', 3, 'view_group'),
(13, 'Can add user', 4, 'add_user'),
(14, 'Can change user', 4, 'change_user'),
(15, 'Can delete user', 4, 'delete_user'),
(16, 'Can view user', 4, 'view_user'),
(17, 'Can add content type', 5, 'add_contenttype'),
(18, 'Can change content type', 5, 'change_contenttype'),
(19, 'Can delete content type', 5, 'delete_contenttype'),
(20, 'Can view content type', 5, 'view_contenttype'),
(21, 'Can add session', 6, 'add_session'),
(22, 'Can change session', 6, 'change_session'),
(23, 'Can delete session', 6, 'delete_session'),
(24, 'Can view session', 6, 'view_session'),
(25, 'Can add mymodel', 7, 'add_mymodel'),
(26, 'Can change mymodel', 7, 'change_mymodel'),
(27, 'Can delete mymodel', 7, 'delete_mymodel'),
(28, 'Can view mymodel', 7, 'view_mymodel'),
(29, 'Can add student', 8, 'add_student'),
(30, 'Can change student', 8, 'change_student'),
(31, 'Can delete student', 8, 'delete_student'),
(32, 'Can view student', 8, 'view_student'),
(33, 'Can add csv', 9, 'add_csv'),
(34, 'Can change csv', 9, 'change_csv'),
(35, 'Can delete csv', 9, 'delete_csv'),
(36, 'Can view csv', 9, 'view_csv'),
(37, 'Can add transaction', 10, 'add_transaction'),
(38, 'Can change transaction', 10, 'change_transaction'),
(39, 'Can delete transaction', 10, 'delete_transaction'),
(40, 'Can view transaction', 10, 'view_transaction'),
(41, 'Can add librarian', 11, 'add_librarian'),
(42, 'Can change librarian', 11, 'change_librarian'),
(43, 'Can delete librarian', 11, 'delete_librarian'),
(44, 'Can view librarian', 11, 'view_librarian'),
(45, 'Can add counts', 12, 'add_counts'),
(46, 'Can change counts', 12, 'change_counts'),
(47, 'Can delete counts', 12, 'delete_counts'),
(48, 'Can view counts', 12, 'view_counts'),
(49, 'Can add book_bank', 13, 'add_book_bank'),
(50, 'Can change book_bank', 13, 'change_book_bank'),
(51, 'Can delete book_bank', 13, 'delete_book_bank'),
(52, 'Can view book_bank', 13, 'view_book_bank'),
(53, 'Can add accountant', 14, 'add_accountant'),
(54, 'Can change accountant', 14, 'change_accountant'),
(55, 'Can delete accountant', 14, 'delete_accountant'),
(56, 'Can view accountant', 14, 'view_accountant'),
(57, 'Can add request_transaction', 10, 'add_request_transaction'),
(58, 'Can change request_transaction', 10, 'change_request_transaction'),
(59, 'Can delete request_transaction', 10, 'delete_request_transaction'),
(60, 'Can view request_transaction', 10, 'view_request_transaction'),
(61, 'Can add book_bank_transaction', 15, 'add_book_bank_transaction'),
(62, 'Can change book_bank_transaction', 15, 'change_book_bank_transaction'),
(63, 'Can delete book_bank_transaction', 15, 'delete_book_bank_transaction'),
(64, 'Can view book_bank_transaction', 15, 'view_book_bank_transaction');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user`
--

CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$150000$rFEnsR3TZGpk$TOHmIgY6XVh3qkI3zv6FA/M4+xz9gODmn0qpCvcPlLA=', '2019-10-01 07:28:05.050682', 1, 'aakash', '', '', 'aakashtolani80@gmail.com', 1, 1, '2019-07-04 07:53:09.987494'),
(2, 'pbkdf2_sha256$150000$ADg3xtwkwgzd$r5XhOzGGQ6z3MurrWyGsoT2vcGYoY9Nb0LHL4XrKhkQ=', NULL, 0, 'sankalp', '', '', '', 0, 1, '2019-07-04 17:28:32.823862');

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_groups`
--

CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `auth_user_user_permissions`
--

CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `book_bank`
--

CREATE TABLE `book_bank` (
  `id` int(11) NOT NULL,
  `semester` int(11) NOT NULL,
  `subjects` varchar(60) NOT NULL,
  `books_names` varchar(200) NOT NULL,
  `books_ssn_numbers` varchar(40) NOT NULL,
  `books_authors` varchar(100) NOT NULL,
  `calendar` varchar(10) NOT NULL,
  `stream` varchar(10) NOT NULL,
  `books_prices` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `book_bank`
--

INSERT INTO `book_bank` (`id`, `semester`, `subjects`, `books_names`, `books_ssn_numbers`, `books_authors`, `calendar`, `stream`, `books_prices`) VALUES
(13, 5, 'java, ds', 'java, ds', 'java ssn, ds ssn', 'java author, ds authn', 's19', 'mca', '200, 100'),
(14, 8, 'java', 'mar java mit java', '8989', 'koi nai', 's19', 'imca', '90');

-- --------------------------------------------------------

--
-- Table structure for table `book_bank_transaction`
--

CREATE TABLE `book_bank_transaction` (
  `id` int(11) NOT NULL,
  `books` varchar(500) NOT NULL,
  `studentt_id` int(11) NOT NULL,
  `bookbank_id` int(11) NOT NULL,
  `prices` varchar(50) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

-- --------------------------------------------------------

--
-- Table structure for table `counts`
--

CREATE TABLE `counts` (
  `id` int(11) NOT NULL,
  `ica_counts` int(11) NOT NULL,
  `mca_counts` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `counts`
--

INSERT INTO `counts` (`id`, `ica_counts`, `mca_counts`) VALUES
(1, 5, 10);

-- --------------------------------------------------------

--
-- Table structure for table `django_admin_log`
--

CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) UNSIGNED NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_admin_log`
--

INSERT INTO `django_admin_log` (`id`, `action_time`, `object_id`, `object_repr`, `action_flag`, `change_message`, `content_type_id`, `user_id`) VALUES
(1, '2019-07-04 07:54:58.778581', '10', 'mymodel object (10)', 1, '[{\"added\": {}}]', 7, 1),
(2, '2019-07-04 17:28:33.010616', '2', 'sankalp', 1, '[{\"added\": {}}]', 4, 1),
(3, '2019-07-05 14:57:58.110903', '9', 'mymodel object (9)', 2, '[{\"changed\": {\"fields\": [\"image\"]}}]', 7, 1),
(4, '2019-07-05 18:48:15.326632', '1', 'student object (1)', 1, '[{\"added\": {}}]', 8, 1),
(5, '2019-07-06 09:38:01.457138', '12', 'student object (12)', 1, '[{\"added\": {}}]', 8, 1),
(6, '2019-07-26 15:03:53.800804', '21', 'student object (21)', 3, '', 8, 1),
(7, '2019-07-26 15:57:37.920936', '24', 'student object (24)', 1, '[{\"added\": {}}]', 8, 1),
(8, '2019-07-27 17:09:42.143059', '3', 'transaction object (3)', 3, '', 10, 1),
(9, '2019-07-27 17:09:48.221202', '2', 'transaction object (2)', 3, '', 10, 1),
(10, '2019-07-27 17:15:40.889354', '4', 'transaction object (4)', 3, '', 10, 1),
(11, '2019-07-28 11:16:31.368291', '1', 'transaction object (1)', 3, '', 10, 1),
(12, '2019-07-29 19:49:46.027902', '1', 'transaction object (1)', 1, '[{\"added\": {}}]', 10, 1),
(13, '2019-07-29 19:55:38.231956', '1', 'transaction object (1)', 2, '[{\"changed\": {\"fields\": [\"status\"]}}]', 10, 1),
(14, '2019-07-29 19:56:31.159332', '1', 'transaction object (1)', 2, '[{\"changed\": {\"fields\": [\"action_date\"]}}]', 10, 1),
(15, '2019-07-29 19:59:19.213209', '2', 'transaction object (2)', 1, '[{\"added\": {}}]', 10, 1),
(16, '2019-08-01 19:37:43.171035', '1', 'transaction object (1)', 3, '', 10, 1),
(17, '2019-08-01 20:52:37.464823', '5', 'transaction object (5)', 3, '', 10, 1),
(18, '2019-08-02 09:40:03.913853', '2', 'transaction object (2)', 3, '', 10, 1),
(19, '2019-09-17 21:14:50.018913', '8', 'transaction object (8)', 3, '', 10, 1),
(20, '2019-09-20 15:31:40.029109', '12', 'transaction object (12)', 1, '[{\"added\": {}}]', 10, 1),
(21, '2019-09-20 15:32:10.980233', '12', 'transaction object (12)', 3, '', 10, 1),
(22, '2019-09-20 15:37:15.192776', '11', 'transaction object (11)', 2, '[{\"changed\": {\"fields\": [\"receipt_no\", \"application_no\"]}}]', 10, 1),
(23, '2019-10-01 06:38:48.243476', '10', 'book_bank object (10)', 3, '', 13, 1),
(24, '2019-10-01 06:51:25.393264', '14', 'transaction object (14)', 2, '[{\"changed\": {\"fields\": [\"status\", \"reason\"]}}]', 10, 1),
(25, '2019-10-01 07:01:26.328268', '14', 'transaction object (14)', 2, '[{\"changed\": {\"fields\": [\"status\"]}}]', 10, 1),
(26, '2019-10-01 07:02:37.087036', '14', 'transaction object (14)', 2, '[{\"changed\": {\"fields\": [\"status\"]}}]', 10, 1),
(27, '2019-10-01 07:12:10.849661', '16', 'student object (16)', 2, '[{\"changed\": {\"fields\": [\"password\", \"phone_no\", \"parents_phone_no\"]}}]', 8, 1),
(28, '2019-10-01 07:29:40.149665', '16', 'student object (16)', 2, '[{\"changed\": {\"fields\": [\"password\"]}}]', 8, 1),
(29, '2019-10-08 20:34:42.246864', '16', 'request_transaction object (16)', 3, '', 10, 1),
(30, '2019-10-08 21:38:08.571678', '17', 'request_transaction object (17)', 3, '', 10, 1),
(31, '2019-10-09 06:02:33.635045', '18', 'request_transaction object (18)', 3, '', 10, 1),
(32, '2019-10-09 06:12:49.775521', '19', 'request_transaction object (19)', 3, '', 10, 1),
(33, '2019-10-09 06:14:51.247983', '20', 'request_transaction object (20)', 3, '', 10, 1),
(34, '2019-10-11 21:32:27.138750', '21', 'request_transaction object (21)', 3, '', 10, 1),
(35, '2019-10-11 21:58:42.460016', '22', 'request_transaction object (22)', 3, '', 10, 1);

-- --------------------------------------------------------

--
-- Table structure for table `django_content_type`
--

CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `app_label`, `model`) VALUES
(1, 'admin', 'logentry'),
(3, 'auth', 'group'),
(2, 'auth', 'permission'),
(4, 'auth', 'user'),
(5, 'contenttypes', 'contenttype'),
(14, 'django_app', 'accountant'),
(13, 'django_app', 'book_bank'),
(15, 'django_app', 'book_bank_transaction'),
(12, 'django_app', 'counts'),
(9, 'django_app', 'csv'),
(11, 'django_app', 'librarian'),
(7, 'django_app', 'mymodel'),
(10, 'django_app', 'request_transaction'),
(8, 'django_app', 'student'),
(6, 'sessions', 'session');

-- --------------------------------------------------------

--
-- Table structure for table `django_migrations`
--

CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_migrations`
--

INSERT INTO `django_migrations` (`id`, `app`, `name`, `applied`) VALUES
(1, 'contenttypes', '0001_initial', '2019-06-29 13:12:12.806207'),
(2, 'auth', '0001_initial', '2019-06-29 13:12:13.005536'),
(3, 'admin', '0001_initial', '2019-06-29 13:12:13.376611'),
(4, 'admin', '0002_logentry_remove_auto_add', '2019-06-29 13:12:13.487823'),
(5, 'admin', '0003_logentry_add_action_flag_choices', '2019-06-29 13:12:13.500696'),
(6, 'contenttypes', '0002_remove_content_type_name', '2019-06-29 13:12:13.567110'),
(7, 'auth', '0002_alter_permission_name_max_length', '2019-06-29 13:12:13.615640'),
(8, 'auth', '0003_alter_user_email_max_length', '2019-06-29 13:12:13.671268'),
(9, 'auth', '0004_alter_user_username_opts', '2019-06-29 13:12:13.690695'),
(10, 'auth', '0005_alter_user_last_login_null', '2019-06-29 13:12:13.712536'),
(11, 'auth', '0006_require_contenttypes_0002', '2019-06-29 13:12:13.715205'),
(12, 'auth', '0007_alter_validators_add_error_messages', '2019-06-29 13:12:13.728589'),
(13, 'auth', '0008_alter_user_username_max_length', '2019-06-29 13:12:13.782357'),
(14, 'auth', '0009_alter_user_last_name_max_length', '2019-06-29 13:12:13.838867'),
(15, 'auth', '0010_alter_group_name_max_length', '2019-06-29 13:12:13.895344'),
(16, 'auth', '0011_update_proxy_permissions', '2019-06-29 13:12:13.915063'),
(17, 'sessions', '0001_initial', '2019-06-29 13:12:13.943995'),
(18, 'django_app', '0001_initial', '2019-06-29 15:29:54.722475'),
(19, 'django_app', '0002_auto_20190703_1643', '2019-07-03 16:44:14.237391'),
(20, 'django_app', '0003_auto_20190704_1456', '2019-07-04 14:57:01.232687'),
(21, 'django_app', '0004_auto_20190704_1457', '2019-07-04 14:58:01.256272'),
(22, 'django_app', '0005_mymodel_image', '2019-07-04 18:44:27.509558'),
(23, 'django_app', '0006_auto_20190705_1456', '2019-07-05 18:46:41.992207'),
(24, 'django_app', '0007_student', '2019-07-05 18:46:42.036690'),
(25, 'django_app', '0008_csv', '2019-07-06 15:47:24.492639'),
(26, 'django_app', '0009_delete_csv', '2019-07-06 20:48:07.329802'),
(27, 'django_app', '0010_transaction', '2019-07-07 11:41:13.344397'),
(28, 'django_app', '0011_auto_20190707_1325', '2019-07-07 13:25:23.084952'),
(29, 'django_app', '0011_auto_20190707_1655', '2019-07-07 16:55:44.410425'),
(30, 'django_app', '0012_auto_20190707_1803', '2019-07-07 18:03:28.415641'),
(31, 'django_app', '0013_student_email', '2019-07-10 16:19:59.270249'),
(32, 'django_app', '0014_librarian', '2019-07-12 12:01:14.721901'),
(33, 'django_app', '0015_auto_20190717_1949', '2019-07-17 19:49:48.855838'),
(34, 'django_app', '0016_auto_20190718_0710', '2019-07-18 07:11:11.990144'),
(35, 'django_app', '0017_auto_20190718_0741', '2019-07-18 07:41:39.104825'),
(36, 'django_app', '0018_auto_20190721_2136', '2019-07-21 21:41:41.926065'),
(37, 'django_app', '0019_auto_20190721_2138', '2019-07-21 21:41:41.953881'),
(38, 'django_app', '0020_transaction_reason', '2019-07-23 12:57:17.478827'),
(39, 'django_app', '0021_auto_20190723_1458', '2019-07-23 14:58:35.296203'),
(40, 'django_app', '0022_auto_20190723_1503', '2019-07-23 15:03:48.176473'),
(41, 'django_app', '0023_auto_20190723_1517', '2019-07-23 15:18:15.305643'),
(42, 'django_app', '0024_auto_20190726_1145', '2019-07-26 11:45:22.667831'),
(43, 'django_app', '0025_transaction_action_date', '2019-07-26 12:29:04.576048'),
(44, 'django_app', '0026_auto_20190726_1556', '2019-07-26 15:56:44.882410'),
(45, 'django_app', '0027_auto_20190727_1713', '2019-07-27 17:14:05.245985'),
(46, 'django_app', '0028_auto_20190727_1850', '2019-07-27 18:50:30.464390'),
(47, 'django_app', '0029_auto_20190728_1637', '2019-07-28 16:38:01.342419'),
(48, 'django_app', '0030_auto_20190801_1858', '2019-08-01 18:58:44.762313'),
(49, 'django_app', '0031_remove_student_application_no', '2019-08-01 19:23:44.069713'),
(50, 'django_app', '0032_counts', '2019-08-01 19:25:59.548525'),
(51, 'django_app', '0033_auto_20190801_1926', '2019-08-01 19:27:13.344025'),
(52, 'django_app', '0034_transaction_additional_information', '2019-08-03 19:41:31.135251'),
(53, 'django_app', '0035_auto_20190803_2117', '2019-08-03 21:17:26.439800'),
(54, 'django_app', '0036_book_bank', '2019-08-10 21:05:24.899712'),
(55, 'django_app', '0037_auto_20190823_2050', '2019-08-23 20:50:37.494656'),
(56, 'django_app', '0038_transaction_temp', '2019-08-23 21:10:54.086611'),
(57, 'django_app', '0039_remove_transaction_temp', '2019-08-24 10:16:55.314928'),
(58, 'django_app', '0040_auto_20190915_2052', '2019-09-15 20:52:58.024893'),
(59, 'django_app', '0041_auto_20190918_1258', '2019-09-18 13:01:12.448709'),
(60, 'django_app', '0042_auto_20190920_1812', '2019-09-20 18:12:34.919034'),
(61, 'django_app', '0043_auto_20190920_1831', '2019-09-20 18:31:40.678484'),
(62, 'django_app', '0044_auto_20190926_1103', '2019-09-26 11:04:07.400514'),
(63, 'django_app', '0045_auto_20190926_1129', '2019-09-26 11:30:02.308071'),
(64, 'django_app', '0046_auto_20190926_1131', '2019-09-26 11:31:56.575263'),
(65, 'django_app', '0047_auto_20191007_1145', '2019-10-07 11:46:03.301724'),
(66, 'django_app', '0048_auto_20191007_1148', '2019-10-07 11:48:24.571276'),
(67, 'django_app', '0049_book_bank_transaction', '2019-10-08 18:50:57.655209'),
(68, 'django_app', '0050_book_bank_transaction_studentt', '2019-10-08 18:50:57.680112'),
(69, 'django_app', '0051_book_bank_books_prices', '2019-10-08 19:00:01.422025'),
(70, 'django_app', '0052_book_bank_transaction_bookbank', '2019-10-08 19:34:36.807837'),
(71, 'django_app', '0053_book_bank_transaction_prices', '2019-10-08 21:12:15.507591');

-- --------------------------------------------------------

--
-- Table structure for table `django_session`
--

CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('6kpfe3pyshv4nl5a9jcd36lkqd3pkdy4', 'MGZjZjI2YzQxZDZlNmQ2YTE3YjVjOWQyY2E1ZWQxYjJlZTFmZjIyODp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI1ZjQ3MTJmMWY2YWJlYmQ5NGY4Zjc4N2I4YWNmNGU3MjU2ODcxM2Y2IiwiY2FwdCI6Ijg2MjkiLCJuYW1lIjoibWVlbmEiLCJlbnJvbGxtZW50IjoiMDA5MCJ9', '2019-08-01 17:25:22.115496'),
('95m3y696pynmq86upqus4vu9bkg67t7o', 'MDZmMzI4MWVlN2E4ZjU0Nzk2YzhlOTFjMGFjZGYzODg5YzJiNTBjZDp7ImNhcHQiOiIxNjI5IiwibmFtZSI6Im1lZW5hIiwiZW5yb2xsbWVudCI6IjAwOTAifQ==', '2019-08-01 17:27:32.168905'),
('cbtkcuwqrpul3kpb78znj6tqetp2aho4', 'ODM3YjQxNzFkMTI2ZWEzNGYwYWViOGJhZmI4Mzc4YmUwNTVjYTY2Mjp7ImNhcHQiOiI0NTA0In0=', '2019-08-01 17:30:46.051754'),
('i6tmcoacpcuxzxg3i9fdatdpuczpvd29', 'YTFlZDE1M2RiOWJlYjlhMTNjYTUxYmViNGE1YzAxM2FkZjBhYTU1YTp7ImNhcHQiOiIyMDExIn0=', '2019-08-01 17:25:50.828287'),
('si4qin5d7ivh71088naqwcorrqik85dk', 'ZDk0M2I5MzQ1ZWYwYWJjZWE1N2M4MjUyOTlmYWY3ZThiYWMxY2U0MDp7ImNhcHQiOiIyNzYzIiwiX2F1dGhfdXNlcl9pZCI6IjEiLCJfYXV0aF91c2VyX2JhY2tlbmQiOiJkamFuZ28uY29udHJpYi5hdXRoLmJhY2tlbmRzLk1vZGVsQmFja2VuZCIsIl9hdXRoX3VzZXJfaGFzaCI6IjVmNDcxMmYxZjZhYmViZDk0ZjhmNzg3YjhhY2Y0ZTcyNTY4NzEzZjYiLCJsaWJfbmFtZSI6InN1YmFzaCIsImxpYl91c2VybmFtZSI6InN1YmFzaGJybyJ9', '2019-09-07 09:56:52.810532'),
('tsas2y0fh7s1auq0dfgb8hdkjanj3yy1', 'NjVjYzZlMjkyYjg1NDZhM2U0ZThlM2UwZTk5YTYxNWU2NzFlMTEzODp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiI1ZjQ3MTJmMWY2YWJlYmQ5NGY4Zjc4N2I4YWNmNGU3MjU2ODcxM2Y2IiwibGliX25hbWUiOiJzdWJhc2giLCJsaWJfdXNlcm5hbWUiOiJzdWJhc2hicm8ifQ==', '2019-11-05 12:54:14.959720');

-- --------------------------------------------------------

--
-- Table structure for table `employ`
--

CREATE TABLE `employ` (
  `id` int(11) NOT NULL,
  `eid` int(11) NOT NULL,
  `ename` varchar(20) NOT NULL,
  `email` varchar(254) NOT NULL,
  `image` varchar(100) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `employ`
--

INSERT INTO `employ` (`id`, `eid`, `ename`, `email`, `image`) VALUES
(9, 34, 'hina beti', 'hina@beti.com', 'image/IMG_3907.JPG'),
(10, 5, 'akas', 'tolani@akas.com', 'null'),
(14, 32, 'hijak laden', 'fjhf@kjh.com', 'null');

-- --------------------------------------------------------

--
-- Table structure for table `librarian`
--

CREATE TABLE `librarian` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL,
  `username` varchar(15) NOT NULL,
  `password` varchar(21) NOT NULL,
  `email` varchar(254) NOT NULL,
  `phone_no` varchar(13) DEFAULT NULL,
  `resi_address` varchar(150) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `librarian`
--

INSERT INTO `librarian` (`id`, `name`, `username`, `password`, `email`, `phone_no`, `resi_address`) VALUES
(1, 'subash', 'subash', 'subash', 'tolaniaakash80@gmail.com', NULL, 'ahmedabad');

-- --------------------------------------------------------

--
-- Table structure for table `request_transaction`
--

CREATE TABLE `request_transaction` (
  `id` int(11) NOT NULL,
  `date` datetime(6) DEFAULT NULL,
  `receipt_no` int(11) DEFAULT NULL,
  `receipt_date` date DEFAULT NULL,
  `amount` int(11) NOT NULL,
  `student_enrollment` varchar(15) NOT NULL,
  `status` varchar(15) NOT NULL,
  `fee_receipt_image` varchar(100) NOT NULL,
  `cancelled_cheque_image` varchar(100) NOT NULL,
  `grade_history_image` varchar(100) NOT NULL,
  `last_sem_fee_image` varchar(100) NOT NULL,
  `passbook_image` varchar(100) NOT NULL,
  `reason` varchar(256) DEFAULT NULL,
  `action_date` datetime(6) DEFAULT NULL,
  `application_no` varchar(15) NOT NULL,
  `additional_information` varchar(150) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `request_transaction`
--

INSERT INTO `request_transaction` (`id`, `date`, `receipt_no`, `receipt_date`, `amount`, `student_enrollment`, `status`, `fee_receipt_image`, `cancelled_cheque_image`, `grade_history_image`, `last_sem_fee_image`, `passbook_image`, `reason`, `action_date`, `application_no`, `additional_information`) VALUES
(14, '2019-09-20 17:56:21.762333', NULL, NULL, 2330, '2343', 'approved', '', 'images/OBZF2262_ACDLFkH.JPG', 'images/IMG_3907_rivy3YZ.JPG', '', 'images/IMG_3907.JPG', 'bas hamari marzi\ngrade history missing', '2019-10-11 21:11:02.362529', 'ica_3', NULL),
(15, '2019-10-07 11:51:06.503415', 2, '2017-02-25', 2950, '175170693016', 'approved', 'images/IMG_3907_iX4yxnN.JPG', 'images/IMG_3907_qA5LKjl.JPG', 'images/IMG_3907_kiftYKQ.JPG', 'images/IMG_3907_EP7NxPc.JPG', 'images/IMG_3907_bpg1ZgN.JPG', NULL, '2019-10-11 21:55:51.992382', 'ica_4', 'bas kuch nai'),
(23, '2019-10-11 22:01:39.606504', NULL, NULL, 2800, '0090', 'pending', '', 'images/OBZF2262.JPG', 'images/IMG_3907_ICRv1YN.JPG', '', 'images/Screenshot_2019-10-09_at_14.46.27.png', NULL, NULL, 'mca_9', NULL);

-- --------------------------------------------------------

--
-- Table structure for table `student`
--

CREATE TABLE `student` (
  `id` int(11) NOT NULL,
  `name` varchar(150) NOT NULL,
  `enrollment` varchar(15) NOT NULL,
  `password` varchar(21) DEFAULT NULL,
  `email` varchar(254) NOT NULL,
  `division` varchar(5) NOT NULL,
  `phone_no` varchar(13) DEFAULT NULL,
  `resi_address` varchar(150) NOT NULL,
  `rollno` int(11) NOT NULL,
  `semester` int(11) NOT NULL,
  `parents_phone_no` varchar(13) NOT NULL,
  `stream` varchar(5) NOT NULL,
  `batch_year` int(11) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;

--
-- Dumping data for table `student`
--

INSERT INTO `student` (`id`, `name`, `enrollment`, `password`, `email`, `division`, `phone_no`, `resi_address`, `rollno`, `semester`, `parents_phone_no`, `stream`, `batch_year`) VALUES
(12, 'akas', '175170693016', 'tolani', 'tolaniaakash8@gmail.com', 'a', NULL, 'ahmedabad', 0, 5, '', 'ica', 2017),
(16, 'meena ashokkumar tol', '0090', 'tolani', 'tolaniaakash80@gmail.com', 'a', '9999999999', 'ahmedabad', 0, 5, '9999999999', 'mca', 2017),
(17, 'ravi', '2343', 'tolani', 'tolaniaakash0@gmail.com', 'a', NULL, 'ahmedabad', 0, 5, '', 'ica', 2017),
(18, 'someone', '007', NULL, 'tolaniaakas80@gmail.com', 'b', '89988989', 'ahmedabad', 36, 5, '', 'ica', 2017),
(22, 'for pagination', '9898', NULL, 'pagination@django.com', 'c', '989823', 'award, kubernagar', 33, 5, '', 'ica', 2017),
(23, 'ashok', '134224', 'tolani', 'tolaniaakas8@gmail.com', 'b', '89898', 'surat', 40, 4, '', 'ica', 2017),
(24, 'dslf', '898', NULL, 'kuchbhi@kuchbhi.com', 'a', '9823', 'charanagar', 33, 5, '', 'ica', 2017),
(28, 'someone', '13424', '', 'email@email.com', 'b', '89898', 'surat', 40, 4, '846058', 'mca', 2017);

--
-- Indexes for dumped tables
--

--
-- Indexes for table `accountant`
--
ALTER TABLE `accountant`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `username` (`username`),
  ADD UNIQUE KEY `email` (`email`);

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
-- Indexes for table `book_bank`
--
ALTER TABLE `book_bank`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `book_bank_stream_calender_semester_c15845ea_uniq` (`stream`,`calendar`,`semester`);

--
-- Indexes for table `book_bank_transaction`
--
ALTER TABLE `book_bank_transaction`
  ADD PRIMARY KEY (`id`),
  ADD KEY `book_bank_transaction_studentt_id_27f0b41e_fk_student_id` (`studentt_id`),
  ADD KEY `book_bank_transaction_bookbank_id_242cfb19_fk_book_bank_id` (`bookbank_id`);

--
-- Indexes for table `counts`
--
ALTER TABLE `counts`
  ADD PRIMARY KEY (`id`);

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
-- Indexes for table `employ`
--
ALTER TABLE `employ`
  ADD PRIMARY KEY (`id`);

--
-- Indexes for table `librarian`
--
ALTER TABLE `librarian`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `librarian_username_5e234ef7_uniq` (`username`),
  ADD UNIQUE KEY `librarian_email_00c4ac71_uniq` (`email`);

--
-- Indexes for table `request_transaction`
--
ALTER TABLE `request_transaction`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `transation_student_enrollment_2e4f31eb_uniq` (`student_enrollment`);

--
-- Indexes for table `student`
--
ALTER TABLE `student`
  ADD PRIMARY KEY (`id`),
  ADD UNIQUE KEY `student_enrollment_5eedd1b3_uniq` (`enrollment`),
  ADD UNIQUE KEY `student_email_76e7ca2e_uniq` (`email`);

--
-- AUTO_INCREMENT for dumped tables
--

--
-- AUTO_INCREMENT for table `accountant`
--
ALTER TABLE `accountant`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `auth_group`
--
ALTER TABLE `auth_group`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_permission`
--
ALTER TABLE `auth_permission`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=65;

--
-- AUTO_INCREMENT for table `auth_user`
--
ALTER TABLE `auth_user`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=3;

--
-- AUTO_INCREMENT for table `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `book_bank`
--
ALTER TABLE `book_bank`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `book_bank_transaction`
--
ALTER TABLE `book_bank_transaction`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT;

--
-- AUTO_INCREMENT for table `counts`
--
ALTER TABLE `counts`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=36;

--
-- AUTO_INCREMENT for table `django_content_type`
--
ALTER TABLE `django_content_type`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=16;

--
-- AUTO_INCREMENT for table `django_migrations`
--
ALTER TABLE `django_migrations`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=72;

--
-- AUTO_INCREMENT for table `employ`
--
ALTER TABLE `employ`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=15;

--
-- AUTO_INCREMENT for table `librarian`
--
ALTER TABLE `librarian`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=2;

--
-- AUTO_INCREMENT for table `request_transaction`
--
ALTER TABLE `request_transaction`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=24;

--
-- AUTO_INCREMENT for table `student`
--
ALTER TABLE `student`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=29;

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
-- Constraints for table `book_bank_transaction`
--
ALTER TABLE `book_bank_transaction`
  ADD CONSTRAINT `book_bank_transaction_bookbank_id_242cfb19_fk_book_bank_id` FOREIGN KEY (`bookbank_id`) REFERENCES `book_bank` (`id`),
  ADD CONSTRAINT `book_bank_transaction_studentt_id_27f0b41e_fk_student_id` FOREIGN KEY (`studentt_id`) REFERENCES `student` (`id`);

--
-- Constraints for table `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
