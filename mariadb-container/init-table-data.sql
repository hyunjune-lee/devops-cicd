-- Database: `daily_quiz`

-- Table structure for table `quiz`

CREATE TABLE IF NOT EXISTS `quiz` (
    `quiz_id` bigint NOT NULL AUTO_INCREMENT,
    `quiz_question` varchar(255) DEFAULT NULL,
    `quiz_answer` varchar(255) DEFAULT NULL,
    `quiz_review_date` date DEFAULT NULL,
    PRIMARY KEY (`quiz_id`)
    ) ENGINE=InnoDB AUTO_INCREMENT=1 DEFAULT CHARSET=utf8 ;

-- Dumping data for table `quiz`

INSERT INTO `quiz` (
    `quiz_id`,`quiz_question`,`quiz_answer`, `quiz_review_date`)
    values
    (1,'What is flask?','Flask is a micro web framework written in Python. It is classified as a microframework because it does not require particular tools or libraries.', NOW());


INSERT INTO `quiz` (
    `quiz_id`,`quiz_question`,`quiz_answer`, `quiz_review_date`)
    values
    (2,'What is JavaScript?','JavaScript often abbreviated as JS, is a programming language that conforms to the ECMAScript specification.', NOW());


INSERT INTO `quiz` (
    `quiz_id`,`quiz_question`,`quiz_answer`, `quiz_review_date`)
    values
    (3,'what is python?','Python is an interpreted, object-oriented, high-level programming language with dynamic semantics.
', NOW());
