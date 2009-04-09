-- phpMyAdmin SQL Dump
-- version 2.11.6
-- http://www.phpmyadmin.net
--
-- Host: localhost
-- Generation Time: Apr 08, 2009 at 06:29 AM
-- Server version: 5.0.51
-- PHP Version: 5.2.6

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- Database: `mysql`
--

-- --------------------------------------------------------

--
-- Table structure for table `words`
--

CREATE TABLE `words` (
  `wordid` int(10) NOT NULL auto_increment,
  `word` varchar(100) NOT NULL,
  `category` varchar(50) NOT NULL,
  `tags` varchar(500) NOT NULL,
  PRIMARY KEY  (`wordid`)
) ENGINE=MyISAM  DEFAULT CHARSET=latin1 AUTO_INCREMENT=103 ;

--
-- Dumping data for table `words`
--

INSERT INTO `words` (`wordid`, `word`, `category`, `tags`) VALUES
(1, 'I', 'Person, Pronoun,', 'Boy, Girl, Human, Man, Men,Women,Child,Children,Ladies,Gentlemen,Woman, Gentleman, Lady, Me, Mine, My'),
(2, 'We', 'Person, Pronoun, Group', 'People, Us, Our, Victory,Success'),
(3, 'You', 'Person, Pronoun', 'Yours, Your, U'),
(4, 'Walk', 'Action, Movement', 'stroll '),
(5, 'Run', 'Action, Movement', 'Sprint, Jog, Jogger, Fled, '),
(6, 'Sleep', 'Position, Rest', 'Rest, Yawn, Dream, Bored'),
(7, 'Eat', 'Action', 'Hog, Swallow, Chew, Churn, Cud, Hungry, Famished, Eatable, Edible, Food, Snacks, Bakery, Restaurant, Gourmet, Glut, Cook, Recipie, Nutrients,'),
(8, 'Drink', 'Action', 'Water, Milk, Pub, Bar, Juice, Liquid, Fluid, Thirsty'),
(9, 'Find', 'Action', 'Search, Clue, Clueless, Crime, Police,'),
(10, 'Jump', 'Action, Movement', 'Elated, Happy, Joy, Hop, Gallop, Yell, Shout, Scream'),
(11, 'Smile', 'Gesture', 'Happy, Joy, Chuckle, Grin, Dimple'),
(12, 'Cry', 'Action', 'Sad, Weep, Mourn, Lament,Pain,Painful'),
(13, 'Giggle', 'Action', 'Laughter, Happiness, Happy, Laugh,Joker,Clown,Mockery,Mock,Joke'),
(15, 'Angry', 'Action', 'Dislike, Hate, Destroy,Terminate,Hulk,Terminator,Destructor,Rude, Mad, Frustrated, Irritated, Disturbed, Tensed, Moody'),
(16, 'Mad', 'Action', 'Idiot, Crazy, Stupid, Lunatic, Asylum, Maniac, Mental, Nuts'),
(17, 'Bend', 'Action, Movement, Greeting', 'Excerise, Pick, Greeting, Respect, Wish'),
(18, 'Exercise', 'Action', 'Lift, Muscles, Workout, Gym, Dumbells, Health, Fitness'),
(19, 'Study', 'Action', 'Academics,Result,School,Exam,Test,College,Education,Books,Read'),
(20, 'Kick', 'Action', 'Kickboxing,Fight.Quarrel,Karate,Marshal,Taekwondo,Boxing'),
(21, 'Punch', 'Action', 'Fight,Quarrel,Beat,Hit,Hurt,Wound,Bruise,Rocky'),
(22, 'Strong', 'Adjective', 'Physique,Muscular,Healthy'),
(23, 'Tired', 'Adjective', 'Fatigue,Weak'),
(24, 'Fly', 'Action', 'Bird,Flight,Float,Wings,'),
(25, 'Punish', 'Action', 'Punishment,Sorry,Forgive,Apologise,Confession,Confess'),
(26, 'Love', 'Gesture', 'Heart,Like,Affection,Cardiac'),
(27, 'Think', 'Action', 'Ponder,Thought,Thinking,Idea,Eureka,Analyze'),
(28, 'Intelligent', 'Adjective', 'Smart,Talented,Einstein,Thomas,Edison,Alber,Isaac,Newton,Bulb,Bright'),
(29, 'Hand', 'Body', 'Arm,Wrist,Palm,Hands,Forearm,Hand,Biceps,Triceps'),
(30, 'Shoulder', 'Body', 'Shoulders'),
(31, 'Torso', 'Body', 'Body,Physique,Figure'),
(32, 'Back', 'Body', 'Spine,Spinal,Cord,'),
(33, 'Elbow', 'Body', 'Elbow'),
(34, 'Fingers', 'Body', 'Thumb,Index,Middle,Pinky,Knuckles,Tickle'),
(38, 'Stomach', 'Body', 'Hungry,Famished,Hog,Eat,Fat,Weight,Obese,Obesity,Foodie'),
(39, 'Thigh', 'Body', 'Thigh,Squats'),
(40, 'Legs', 'Body', 'Calves,Leg,Calf,Knees,Knee,Kick'),
(41, 'Feet', 'Body', 'Feet,Shoes,Shoe,Boot,Boots'),
(42, 'Toes', 'Body', 'Toe,Tips'),
(43, 'Face', 'Body', 'Expression,'),
(44, 'Lips', 'Body', 'Mouth,Teeth,Tooth'),
(45, 'Kiss', 'Verb,Action', 'Flying,French'),
(46, 'Eyes', 'Body', 'Eye,Wink,Blink,Cataract,Conjunctivitis'),
(47, 'Ears', 'Body', 'Ear,Eardrum,Listen,Hear,Sound,Noise'),
(48, 'Nose', 'Body', 'Smell,Stink,Fragrance,Snout'),
(49, 'Cheeks', 'Body', 'Chubby'),
(50, 'Skin', 'Body', 'Skinny'),
(51, 'Pull', 'Verb,Action', 'Drag'),
(52, 'Push', 'Body', 'Force,Forceful,'),
(53, 'Talk', 'Verb,Action', 'Converse,Conversation'),
(54, 'Move', 'Verb,Action', 'Movement,Act,Action,Enact'),
(55, 'Still', 'Adjective', 'Stationary,Fixed,'),
(56, 'Yawn', 'Verb,Action', 'Bored,Sleepy,Boredom'),
(57, 'Turn', 'Verb,Action', 'Twist,Twisted'),
(58, 'Shrug', 'Verb,Action', 'Shrug'),
(59, 'Neck', 'Body', 'Throat,Voice'),
(60, 'Sigh', 'Verb,Action', 'Relief'),
(61, 'Dance', 'Verb,Action', 'Entertainment,Entertain,Holiday,Enjoy,Celebrate,Pleasure,Party'),
(62, 'Yes', 'Gesture,Verb,Action', 'Agree,Agreement,Nod,Noddy'),
(63, 'No', 'Gesture,Verb,Action', 'Disagree,Disagreement,Shake,Shook'),
(64, 'Sing', 'Verb,Action', 'Song,Maestro,Musician,Music,LyricsMelody,Melodious,Tune,Rhythm,Rhythmic,Guitar,Casio,Piano,Mike,Stage,Singer'),
(65, 'Scared', 'Verb,Action', 'Fear,Scary,Scare,Afraid,Scardy,Frightened,Ghost,Spirit,Exhorcist,Exhorcism,'),
(66, 'Play', 'Verb,Action', 'Game,Sports,Volleyball,Ball,Football,Cricket,Soccer,Rugby,Kabaddi,Carrom,Skating,Hockey,Cards'),
(67, 'Hide', 'Verb,Action', 'Seek,'),
(68, 'Yoga', 'Verb,Action', 'Exercise,Relaxation,Relax'),
(69, 'Cross', 'Adjective,Noun', 'Angry,Church,Jesus,Christ,Mary,Holy,Grail,Bible,Joseph'),
(70, 'Hi', 'Greeting,Gesture', 'Bye,Hello,Good,Morning,Afternoon,Evening,Night,Saiyonara,Adios,Chao'),
(71, 'Magic', 'Noun', 'Magical,Enchanted,Fairytale'),
(72, '1', 'Digit', 'One,Single,Singular,Once,First'),
(73, '2', 'Digit', 'Two,Double,Plural,Twice,Second'),
(74, '0', 'Digit', 'None,Null,Zero,Zinch,Nothing,Zeroth'),
(75, '3', 'Digit', 'Three,Triple,Thrice,Third,Tri'),
(76, '4', 'Digit', 'Four,Quadruple,Quad,Quadrant,Quarter,Fourth,Quarterly'),
(77, '5', 'Digit', 'Five,Fifth,Pent'),
(78, '6', 'Digit', 'Six,Sixth,Sixer,Hex'),
(79, '7', 'Digit', 'Seven,Seventh,Hept'),
(80, '8', 'Digit', 'Eight,Eighth,Oct'),
(81, '9', 'Digit', 'Nine,Ninth,Nano,Nona'),
(82, 'Big', 'Adjective', 'Large,Huge,Oversized,Great,Macro,Magnify,Mega,Kilo,Tera,Giga,Bigger,Biggest,Larger,Largest,Gigantic,Giant,Abominable,Snowman'),
(83, 'Small', 'Adjective', 'Micro,Milli,Less,Least,Smaller,Smallest,Some,Few'),
(84, 'Type', 'Verb,Action', 'Computer,Type,Typewriter,PC,Laptop,Job,Work,Do,Done,Doing'),
(85, 'Open', 'Verb,Action', 'Opened'),
(86, 'Close', 'Verb,Action', 'Closed'),
(87, 'Tease', 'Verb,action', 'Irritate,Annoy'),
(88, 'Stop', 'Verb,Action', 'Stopped,Traffic,Signal,Wait'),
(89, 'Next', 'Verb,Action', 'More,Close'),
(90, 'A', 'Article', 'And,An'),
(91, 'The', 'Article', 'The'),
(92, 'In', 'Proposition', 'Inside,Indoor'),
(93, 'Of', 'Proposition', 'Of'),
(94, '', '', ''),
(95, 'See', 'Verb,Action', 'Sight,View,Visible,Visibility,Clear,Clarify,Look'),
(96, 'Animal', 'Noun', 'Bird,Insect,Reptile'),
(97, 'Lift', 'Noun', 'Pickup,Road'),
(98, 'Clap', 'Verb,Action', 'Applaud,Applause,Appreciate,Praise,Encourage,Encouragement'),
(99, 'Pride', 'Adjective', 'Anthem,Proud,Boast,Loyal,Honour'),
(100, 'Salute', 'Gesture,Verb,Action', 'Respect,Honour'),
(101, 'Quiet', 'Adjective', 'Silence,Silent,Sh,Shhh,Sshh,Still'),
(102, 'Rain', 'Noun', 'Monsoon,Shower,Showers,Drizzle,Drizzling');
