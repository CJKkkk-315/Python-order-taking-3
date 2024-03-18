/*
 Navicat Premium Data Transfer

 Source Server         : 127.0.0.1
 Source Server Type    : MySQL
 Source Server Version : 100410
 Source Host           : localhost:3306
 Source Schema         : exam

 Target Server Type    : MySQL
 Target Server Version : 100410
 File Encoding         : 65001

 Date: 10/07/2022 23:25:30
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;


-- ----------------------------
-- Table structure for news
-- ----------------------------
DROP TABLE IF EXISTS `news`;
CREATE TABLE `news`  (
  `news_id` int UNSIGNED NOT NULL AUTO_INCREMENT COMMENT '新闻编号',
  `news_title` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL COMMENT '新闻标题',
  `news_body` text CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL COMMENT '新闻正文',
  `news_author` varchar(255) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT '本网讯' COMMENT '新闻作者',
  `news_date` datetime NULL DEFAULT NULL COMMENT '新闻发表时间',
  PRIMARY KEY (`news_id`) USING BTREE
) ENGINE = MyISAM AUTO_INCREMENT = 10 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of news
-- ----------------------------
INSERT INTO `news` VALUES (1, '一天掉多少根头发', '一天掉多少根头发，发生了会如何，不发生又会如何。 歌德曾经说过，意志坚强的人能把世界放在手中像泥块一样任意揉捏。这不禁令我深思带着这些问题，我们来审视一下一天掉多少根头发。 在这种困难的抉择下，本人思来想去，寝食难安。 生活中，若一天掉多少根头发出现了，我们就不得不考虑它出现了的事实。 一般来说， 一般来讲，我们都必须务必慎重的考虑考虑。 总结的来说， 一般来讲，我们都必须务必慎重的考虑考虑。 既然如何， 而这些并不是完全重要，更加重要的问题是， 问题的关键究竟为何? 一般来说， 就我个人来说，一天掉多少根头发对我的意义，不能不说非常重大。', '本网讯', '2022-06-14 21:18:34');
INSERT INTO `news` VALUES (2, '计算机专业好学吗', '所谓计算机专业好学吗，关键是计算机专业好学吗需要如何写。 计算机专业好学吗，到底应该如何实现。 生活中，若计算机专业好学吗出现了，我们就不得不考虑它出现了的事实。 总结的来说， 要想清楚，计算机专业好学吗，到底是一种怎么样的存在。 计算机专业好学吗的发生，到底需要如何做到，不计算机专业好学吗的发生，又会如何产生。 既然如此， 而这些并不是完全重要，更加重要的问题是， 那么， 孔子曾经说过，知之者不如好之者，好之者不如乐之者。这不禁令我深思要想清楚，计算机专业好学吗，到底是一种怎么样的存在。', '本网讯', '2022-06-16 21:19:00');
INSERT INTO `news` VALUES (3, '如何变得更高', '这不禁令我深思一般来说， 我们一般认为，抓住了问题的关键，其他一切则会迎刃而解。 吉格·金克拉曾经说过，如果你能做梦，你就能实现它。这不禁令我深思了解清楚如何变得更高到底是一种怎么样的存在，是解决一切问题的关键。 如何变得更高，到底应该如何实现。 既然如此， 我们一般认为，抓住了问题的关键，其他一切则会迎刃而解。 所谓如何变得更高，关键是如何变得更高需要如何写。 我们都知道，只要有意义，那么就必须慎重考虑。 问题的关键究竟为何? 这种事实对本人来说意义重大，相信对这个世界也是有一定意义的。', '本网讯', '2022-06-20 21:19:20');
INSERT INTO `news` VALUES (4, '想变成一只飞鸟', '黑塞曾经说过，有勇气承担命运这才是英雄好汉。这不禁令我深思叔本华曾经说过，普通人只想到如何度过时间，有才能的人设法利用时间。这不禁令我深思雷锋曾经说过，自己活着，就是为了使别人过得更美好。这不禁令我深思而这些并不是完全重要，更加重要的问题是， 在这种困难的抉择下，本人思来想去，寝食难安。 要想清楚，想变成一只飞鸟，到底是一种怎么样的存在。 拉罗什福科曾经说过，我们唯一不会改正的缺点是软弱。这不禁令我深思想变成一只飞鸟的发生，到底需要如何做到，不想变成一只飞鸟的发生，又会如何产生。 想变成一只飞鸟因何而发生?就我个人来说，想变成一只飞鸟对我的意义，不能不说非常重大。', '本网讯', '2022-06-22 21:19:42');
INSERT INTO `news` VALUES (5, '世界上有多少老实人', '我们小时候都听过《东郭先生和狼》的故事，故事里的东郭先生就是这样一个没有心机的老实人，因为听信了狼的谗言，帮助狼躲过了猎人。但是自己却被狼吃了。\r\n所以，老实人，还是长点心吧，太过老实，在社会中，只能成为别人的炮灰。', '本网讯', '2022-06-27 21:20:01');
INSERT INTO `news` VALUES (6, '学什么技术有前途', '越来越多的年轻人涉足纹绣行业，现在学习纹绣的人数在不断扩大。那么学习纹绣有前途吗？纹绣师有前途吗？在文章《纹绣行业发展趋势》中数据显示，纹绣师是美近年来继纹绣师和纹绣划分之后的又一热门职业。其作品轻松时尚，深受现代年轻人的青睐。为了让美的客人更漂亮，纹绣师的主要工作是根据顾客的年龄、气质、职业、喜好、手型、指甲形状和肤质，设计出不同特色的纹绣（眉、眼、唇），丰富了人体形象设计的美，满足了人们对美的追求。那么想要加入纹绣行业需要怎么办？学习纹绣有前途吗？纹绣师有前途吗？', '本网讯', '2022-06-28 21:20:17');
INSERT INTO `news` VALUES (7, '如何获得好心情', '心情不好的人全都是因为他们可以发泄情绪的环境，在那些不能容忍他发泄情绪的场合，他们会表现得很好，这表明，要控制自己的情绪，首先要让自己保持平静的心态，不要使用脾气不好的借口。\r\n这根本不是脾气不好的问题，而是自我控制的问题\r\n。', '本网讯', '2022-06-29 21:20:31');
INSERT INTO `news` VALUES (8, '动画片适合成年人吗', '2022年春节，贺岁档电影里出现了几个久违的身影：喜羊羊和灰太狼家族。很多人都没注意到，这些春节档的常客，其实已经7年没在春节的大银幕上出现过了，取而代之的是两只大灰熊和一个光头的伐木工。\r\n儿童向的动画片是贺岁档里从未缺席的类型，只是江湖地位阶段性地发生着更迭。如今雄踞头牌的是《熊出没》，今年春节档的《熊出没·重返地球》狂揽9.78亿元票房，位居档期第四。《喜羊羊与灰太狼之筐出未来》则以不温不火的1.6亿元收官。', '本网讯', '2022-06-30 21:20:44');
INSERT INTO `news` VALUES (9, '半导体产业的发展情况', '半导体产业早期包括集成电路、分立器件、光伏发电和LED照明等产业，由于光伏发电和LED照明产业的制造业特点和规模巨大，已独立统计于半导体产业之外。现在半导体产业仅包括集成电路和分立器件，分立器件在半导体产业中占比很小，说半导体产业基本等同于说集成电路产业。', '本网讯', '2022-07-01 21:20:59');

-- ----------------------------
-- Table structure for users
-- ----------------------------
DROP TABLE IF EXISTS `users`;
CREATE TABLE `users`  (
  `userid` int NOT NULL AUTO_INCREMENT,
  `username` varchar(50) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `password` varchar(32) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `nickname` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `avatar` varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `qq` varchar(15) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NULL DEFAULT NULL,
  `role` varchar(10) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL DEFAULT 'user',
  `credit` int NOT NULL DEFAULT 50,
  `createtime` datetime NULL DEFAULT NULL,
  `updatetime` datetime NULL DEFAULT NULL,
  PRIMARY KEY (`userid`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 51 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Records of users
-- ----------------------------
INSERT INTO `users` VALUES (1, 'woniu@woniuxy.com', 'e10adc3949ba59abbe56e057f20f883e', '蜗牛', '1.png', '12345678', 'admin', 5025, '2020-02-05 12:31:57', '2020-02-12 11:45:57');
INSERT INTO `users` VALUES (2, 'qiang@woniuxy.com', 'e10adc3949ba59abbe56e057f20f883e', '强哥', '2.png', '33445566', 'editor', 548, '2020-02-06 15:16:55', '2020-02-12 11:46:01');
INSERT INTO `users` VALUES (3, 'denny@woniuxy.com', 'e10adc3949ba59abbe56e057f20f883e', '丹尼', '3.png', '226658397', 'user', 81, '2020-02-06 15:17:30', '2020-02-12 11:46:08');
INSERT INTO `users` VALUES (4, 'reader1@woniuxy.com', 'e10adc3949ba59abbe56e057f20f883e', 'reader1', '8.png', '12345678', 'user', 53, '2020-02-16 13:50:12', '2020-02-16 13:50:12');
INSERT INTO `users` VALUES (5, 'reader2@woniuxy.com', 'e10adc3949ba59abbe56e057f20f883e', '张三', '6.png', '12345678', 'user', 77, '2020-02-16 14:56:37', '2020-02-16 14:56:37');
INSERT INTO `users` VALUES (6, 'reader3@woniuxy.com', 'e10adc3949ba59abbe56e057f20f883e', 'reader3', '13.png', '12345678', 'user', 64, '2020-02-16 14:59:12', '2020-02-16 14:59:12');
INSERT INTO `users` VALUES (7, 'tester@woniuxy.com', 'e10adc3949ba59abbe56e057f20f883e', 'tester', '9.png', '12345678', 'user', 59, '2020-02-23 03:38:34', '2020-02-23 03:38:34');
INSERT INTO `users` VALUES (50, 'dengqiang@woniuxy.com', 'e10adc3949ba59abbe56e057f20f883e', 'dengqiang', '3.png', NULL, 'user', 50, '2020-03-31 23:02:43', '2020-03-31 23:02:43');

SET FOREIGN_KEY_CHECKS = 1;
