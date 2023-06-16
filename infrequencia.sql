-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 16/06/2023 às 04:13
-- Versão do servidor: 10.4.28-MariaDB
-- Versão do PHP: 8.2.4

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Banco de dados: `infrequencia`
--

-- --------------------------------------------------------

--
-- Estrutura para tabela `cadastro`
--

CREATE TABLE `cadastro` (
  `id` int(11) NOT NULL,
  `email` varchar(80) NOT NULL,
  `senha` varchar(10) NOT NULL,
  `cargo` varchar(20) NOT NULL,
  `disciplina` varchar(30) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `cadastro`
--

INSERT INTO `cadastro` (`id`, `email`, `senha`, `cargo`, `disciplina`) VALUES
(1, 'Caua', '4545', '', ''),
(2, 'Larissa', 'meianoite', '', ''),
(3, 'Luana', 'mario', '1', ''),
(4, 'Luana', 'mario', '1', ''),
(5, 'Luana', 'mario', '1', ''),
(6, 'Luana', 'mario', '1', ''),
(7, 'Gleyci', 'gato', 'Professor', ''),
(8, 'Lara', 'gatinha', 'Professor', 'portugues'),
(9, 'Thiago', 'safado', 'Coordenação', ''),
(10, 'Vitoria', 'linda', 'Professor', 'Redacao'),
(11, 'Vitoria', 'linda', 'Professor', 'Redacao'),
(13, 'kelly', 'braga', 'Coordenação', ''),
(14, 'lara', 'larinha', 'Professor', 'jdahdksd'),
(15, 'lara', 'tia', 'Professor', 'aham'),
(16, 'unha', 'esmalte', '1', 'pedicure'),
(17, 'salao', 'cabelo', '1', 'eeeeee'),
(18, 'alxmsac', 'scdsdc', '1', 'sdxs'),
(19, 'Lara', 'oioi', 'Professor', 'auau'),
(20, 'sadsad', 'dfdsf', 'Professor', 'sdsd'),
(21, 'sdsad', 'grgfrfg', 'Professor', 'refef'),
(22, 'lkjdsas', '33333333', 'Professor', '3224'),
(23, 'qswdef', 'efef', 'Professor', 'efef'),
(24, 'eewq', 'wewew', 'Coordenação', ''),
(25, 'lara', 'lara', 'Coordenação', ''),
(26, 'luiza', 'mel', 'Coordenação', ''),
(27, 'lara', '1234', 'Professor', 'dfdf'),
(28, 'effr', 'ewfef', 'Coordenação', ''),
(29, 'dfvff', 'fgfgfg', 'Professor', 'def'),
(30, 'ewfdew', 'efef', 'Professor', 'wfwef'),
(31, 'ewfef', 'efef', 'Coordenação', ''),
(32, 'Lidia', 'louca', 'Professor', 'matematica'),
(33, 'Marcleide', 'oi', 'Coordenação', ''),
(34, 'luiza', '1234', 'Coordenação', ''),
(35, 'lucas', 'josy', 'Professor', 'reforco'),
(36, 'Luizinha', '00', 'Coordenação', ''),
(37, '00000', '000000', 'Coordenação', ''),
(38, 'porta', 'porta', 'Coordenação', ''),
(39, 'ddddd', 'ddd', 'Professor', 'eeeee'),
(40, 'Lara', 'teresa', 'Professor', 'jasass');

-- --------------------------------------------------------

--
-- Estrutura para tabela `frequencia`
--

CREATE TABLE `frequencia` (
  `id` int(11) NOT NULL,
  `numero` varchar(10) NOT NULL,
  `nome` varchar(150) NOT NULL,
  `horario` varchar(30) NOT NULL,
  `serie` varchar(10) NOT NULL,
  `data` varchar(36) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `frequencia`
--

INSERT INTO `frequencia` (`id`, `numero`, `nome`, `horario`, `serie`, `data`) VALUES
(54, '04', 'Angelo Gabriel Vieira de Oliveira', '2º', '3º', ''),
(56, '05', 'Angelo Gabriel Vieira de Oliveira', '3º', '3º', ''),
(57, '05', 'Bruno Henrique do Nascimento Firmino', '3º', '3º', ''),
(65, '05', 'Bruno Henrique do Nascimento Firmino', '7º', '3º', ''),
(66, '06', 'Cauã Roberto de Souza', '3º', '3º', ''),
(73, '04', 'Angelo Gabriel Vieira de Oliveira', '4º', '3º', ''),
(77, '02', 'Bruno Henrique do Nascimento Firmino', '4º', '3º', ''),
(78, '03', 'Bruno Henrique do Nascimento Firmino', '4º', '3º', ''),
(81, '03', 'Ashley Darwin de Souza Duarte', '4º', '3º', ''),
(82, '03', 'Lara Evelyn de Sousa Pinto', '3º', '3º', ''),
(83, '10', 'Eric do Nascimento Sousa Diniz', '9º', '3º', ''),
(84, '10', 'Emanoell Edvan Souza da Silva', '4º', '3º', ''),
(85, '10', 'Cauã Roberto de Souza', '8º', '3º', ''),
(88, '06', 'Andressa da Silva Matos', '1º', '3º', ''),
(89, '06', 'Bruno Henrique do Nascimento Firmino', '4º', '3º', ''),
(90, '05', 'Maria Eduarda Castro dos Santos', '6º', '3º', ''),
(91, '05', 'Luana Hevillyn Morais da Silva', '6º', '3º', ''),
(92, '03', 'Bruno Henrique do Nascimento Firmino', '3º', '3º', ''),
(93, '05', 'Ashley Darwin de Souza Duarte', '5º', '3º', '');

-- --------------------------------------------------------

--
-- Estrutura para tabela `login`
--

CREATE TABLE `login` (
  `id` int(11) NOT NULL,
  `nome` varchar(150) NOT NULL,
  `data` varchar(16) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `login`
--

INSERT INTO `login` (`id`, `nome`, `data`) VALUES
(16, 'Caua', '2023-06-05 08:39'),
(17, 'Caua', '2023-06-08 19:08'),
(18, 'Caua', '2023-06-08 19:08'),
(19, 'Caua', '2023-06-08 19:20'),
(20, 'Caua', '2023-06-08 19:21'),
(21, 'Caua', '2023-06-08 19:21'),
(22, 'Caua', '2023-06-08 19:21'),
(23, 'Caua', '2023-06-08 19:22'),
(25, 'Caua', '2023-06-08 19:29'),
(26, 'Caua', '2023-06-08 19:29'),
(27, 'Caua', '2023-06-08 21:16'),
(28, 'Caua', '2023-06-08 21:24'),
(29, 'Larissa', '2023-06-08 21:25'),
(30, 'Lidia', '2023-06-09 19:00'),
(31, 'Marcleide', '2023-06-09 19:01'),
(32, 'lara', '2023-06-09 19:10'),
(33, 'Thiago', '2023-06-09 20:01'),
(34, 'lara', '2023-06-09 20:54'),
(35, 'lara', '2023-06-09 20:56'),
(36, 'Marcleide', '2023-06-10 15:43'),
(37, 'Marcleide', '2023-06-10 15:43'),
(38, 'Marcleide', '2023-06-10 15:43'),
(39, 'Lara', '2023-06-10 15:43'),
(40, 'Marcleide', '2023-06-10 15:47'),
(41, 'Marcleide', '2023-06-10 15:49'),
(42, 'Lara', '2023-06-10 15:49'),
(43, 'Marcleide', '2023-06-10 15:50'),
(44, 'Marcleide', '2023-06-10 15:53'),
(45, 'Lara', '2023-06-10 15:55'),
(46, 'Marcleide', '2023-06-10 16:03'),
(47, 'Marcleide', '2023-06-10 16:05'),
(48, 'Lara', '2023-06-10 16:08'),
(49, 'Marcleide', '2023-06-10 16:08'),
(50, 'Marcleide', '2023-06-10 17:32'),
(51, 'Lara', '2023-06-10 18:17'),
(52, 'Lara', '2023-06-10 18:17'),
(53, 'Lara', '2023-06-10 18:19'),
(54, 'Lara', '2023-06-10 18:20'),
(55, 'Lara', '2023-06-10 18:22'),
(56, 'Lara', '2023-06-10 18:22'),
(57, 'Lara', '2023-06-13 22:46'),
(58, 'Lara ', '2023-06-13 22:59'),
(59, 'Lara', '2023-06-13 23:00'),
(60, 'Lara', '2023-06-15 19:52'),
(61, 'Lara', '2023-06-15 20:32'),
(62, 'Lara', '2023-06-15 20:32');

-- --------------------------------------------------------

--
-- Estrutura para tabela `primeiro`
--

CREATE TABLE `primeiro` (
  `id` int(11) NOT NULL,
  `numero` varchar(3) NOT NULL,
  `nome` varchar(150) NOT NULL,
  `horario` varchar(12) NOT NULL,
  `serie` varchar(10) NOT NULL,
  `data` varchar(36) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `primeiro`
--

INSERT INTO `primeiro` (`id`, `numero`, `nome`, `horario`, `serie`, `data`) VALUES
(7, '08', 'Antonio Caua de Brito Augusto Sales', '6º', '1º', ''),
(8, '05', 'Arthur Rocha da Silva Alves', '2º', '1º', ''),
(9, '06', 'Ana Beatriz Pereira Martins', '3º', '1º', ''),
(10, '10', 'Caio Lucas Moreno Vieira', '6º', '1º', ''),
(11, '08', 'Caio Lucas Moreno Vieira', '3º', '1º', ''),
(12, '44', 'Pedro Henrique de Oliveira Carvalho', '6º', '1º', ''),
(13, '33', 'Laís de Sena Oliveira', '9º', '1º', ''),
(14, '28', 'Átila do Nascimento Rocha', '6º', '1º', ''),
(15, '08', 'Átila do Nascimento Rocha', '7º', '1º', '2023-06-15 19:52:49.533493'),
(16, '08', 'Átila do Nascimento Rocha', '2º', '1º', '2023-06-15 19:53:10.023945');

-- --------------------------------------------------------

--
-- Estrutura para tabela `segundo`
--

CREATE TABLE `segundo` (
  `id` int(11) NOT NULL,
  `numero` varchar(3) NOT NULL,
  `nome` varchar(150) NOT NULL,
  `horario` varchar(5) NOT NULL,
  `serie` varchar(10) NOT NULL,
  `data` varchar(36) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `segundo`
--

INSERT INTO `segundo` (`id`, `numero`, `nome`, `horario`, `serie`, `data`) VALUES
(2, '01', 'Gabriela Angelo Ribeiro', '3º', '2º', '2023-06-15 21:01:39.423137'),
(3, '09', 'Daniel Bezerra Silva Filho', '9º', '2º', ''),
(4, '08', 'Eloisa Braga Farias', '7º', '2º', ''),
(5, '09', 'Daniel Bezerra Silva Filho', '3º', '2º', ''),
(6, '01', 'Gabriela Angelo Ribeiro', '3º', '2º', '2023-06-15 21:01:39.423137'),
(7, '01', 'Adriel Levi de Sousa Vieira', '1º', '2º', ''),
(8, '04', 'Ana Luiza Bezerra de Freitas', '9º', '2º', '2023-06-15 21:03:49.944018'),
(9, '03', 'Antonia Vladia de Sousa Moreira', '6º', '2º', ''),
(10, '08', 'Cleber Lucas da Costa Macedo', '3º', '2º', '2023-06-15 19:57:55.190386'),
(11, '08', 'Cleber Lucas da Costa Macedo', '5º', '2º', '2023-06-15 19:58:12.794529'),
(13, '01', 'Gabriela Angelo Ribeiro', '3º', '2º', '2023-06-15 21:01:39.423137'),
(14, '01', 'Gabriela Angelo Ribeiro', '3º', '2º', '2023-06-15 21:01:39.423137'),
(15, '', '', '', '2º', '2023-06-15 20:52:16.038521'),
(16, '01', 'Gabriela Angelo Ribeiro', '3º', '2º', '2023-06-15 21:01:39.423137'),
(17, '01', 'Gabriela Angelo Ribeiro', '3º', '2º', '2023-06-15 21:01:39.423137'),
(18, '06', 'Gabriela Angelo Ribeiro', '3º', '2º', '2023-06-15 21:00:43.354592'),
(19, '06', 'Gabriela Angelo Ribeiro', '3º', '2º', '2023-06-15 21:00:52.955756'),
(20, '01', 'Gabriela Angelo Ribeiro', '3º', '2º', '2023-06-15 21:01:39.423137'),
(21, '04', 'Ana Luiza Bezerra de Freitas', '9º', '2º', '2023-06-15 21:03:49.944018'),
(23, '04', 'Ana Luiza Bezerra de Freitas', '9º', '2º', '2023-06-15 21:03:49.944018'),
(24, '05', 'Carlos Eduardo de Sousa Lima', '4º', '2º', '2023-06-15 22:19:09.146667'),
(25, '05', 'Carlos Eduardo de Sousa Lima', '4º', '2º', '2023-06-15 22:19:09.146667'),
(26, '06', 'Cleber Lucas da Costa Macedo', '4º', '2º', '2023-06-15 21:39:19.328092'),
(27, '07', 'Antonia Vladia de Sousa Moreira', '3º', '2º', '2023-06-15 21:39:28.846214'),
(28, '06', 'Antonio Anderson Faustino Andre', '4º', '2º', '2023-06-15 21:39:36.029407'),
(29, '04', 'Rikson de Oliveira Justino', '4º', '2º', '2023-06-15 21:44:25.680948'),
(30, '04', 'Carlos Eduardo de Sousa Lima', '2º', '2º', '2023-06-15 21:44:39.088539'),
(31, '04', 'Natanyell Romão Rodrigues', '4º', '2º', '2023-06-15 21:44:50.267566'),
(32, '04', 'Cleber Lucas da Costa Macedo', '4º', '2º', '2023-06-15 21:50:33.130574'),
(33, '', '', '', '2º', '2023-06-15 21:50:38.073250'),
(34, '04', 'Adriel Levi de Sousa Vieira', '4º', '2º', '2023-06-15 21:50:53.304409'),
(35, '04', 'Carlos Eduardo de Sousa Lima', '2º', '2º', '2023-06-15 21:58:02.023578'),
(36, '08', 'Eloisa Braga Farias', '9º', '2º', '2023-06-15 21:58:11.268522'),
(37, '04', 'Davi Moreira Silva', '1º', '2º', '2023-06-15 21:58:20.384105'),
(39, '10', 'Gabriela Angelo Ribeiro', '9º', '2º', '2023-06-15 22:03:53.496819'),
(40, '07', 'Carlos Eduardo de Sousa Lima', '4º', '2º', '2023-06-15 22:04:04.455545'),
(41, '10', 'Gabriela Angelo Ribeiro', '9º', '2º', '2023-06-15 22:04:09.686043'),
(44, '07', 'Cleber Lucas da Costa Macedo', '4º', '2º', '2023-06-15 22:07:02.506617'),
(49, '01', 'Adriel Levi de Sousa Vieira', '1º', '2º', '2023-06-15 22:11:48.545427'),
(50, '01', 'Adriel Levi de Sousa Vieira', '1º', '2º', '2023-06-15 22:11:54.749158'),
(51, '04', 'Antonia Vladia de Sousa Moreira', '2º', '2º', '2023-06-15 22:14:43.602697'),
(52, '04', 'Antonia Vladia de Sousa Moreira', '2º', '2º', '2023-06-15 22:14:57.695286'),
(53, '05', 'Carlos Eduardo de Sousa Lima', '4º', '2º', '2023-06-15 22:19:09.146667'),
(54, '05', 'Carlos Eduardo de Sousa Lima', '4º', '2º', '2023-06-15 22:19:09.146667'),
(55, '02', 'Ana Luiza Bezerra de Freitas', '2º', '2º', '2023-06-15 22:21:32.383678'),
(56, '02', 'Cleber Lucas da Costa Macedo', '2º', '2º', '2023-06-15 22:22:24.114371'),
(57, '04', 'Cleber Lucas da Costa Macedo', '6º', '2º', '2023-06-15 22:26:19.359406'),
(58, '04', 'Cleber Lucas da Costa Macedo', '6º', '2º', '2023-06-15 22:26:49.209718'),
(59, '05', 'Antonia Vladia de Sousa Moreira', '4º', '2º', '2023-06-15 22:29:25.759721'),
(60, '05', 'Antonia Vladia de Sousa Moreira', '4º', '2º', '2023-06-15 22:30:01.767645'),
(62, '07', 'Antonio Anderson Faustino Andre', '6º', '2º', '2023-06-15 23:01:20.904003'),
(63, '07', 'Antonio Anderson Faustino Andre', '6º', '2º', '2023-06-15 23:01:30.023888'),
(64, '07', 'Antonia Vladia de Sousa Moreira', '2º', '2º', '2023-06-15 23:04:43.305021'),
(66, '06', 'Carlos Eduardo de Sousa Lima', '3º', '2º', '2023-06-15 23:05:28.537779'),
(68, '03', 'Ana Luiza Bezerra de Freitas', '2º', '2º', '2023-06-15 23:05:58.050755'),
(69, '03', 'Daniel Bezerra Silva Filho', '2º', '2º', '2023-06-15 23:06:02.428706');

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `cadastro`
--
ALTER TABLE `cadastro`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `frequencia`
--
ALTER TABLE `frequencia`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `login`
--
ALTER TABLE `login`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `primeiro`
--
ALTER TABLE `primeiro`
  ADD PRIMARY KEY (`id`);

--
-- Índices de tabela `segundo`
--
ALTER TABLE `segundo`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `cadastro`
--
ALTER TABLE `cadastro`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=41;

--
-- AUTO_INCREMENT de tabela `frequencia`
--
ALTER TABLE `frequencia`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=94;

--
-- AUTO_INCREMENT de tabela `login`
--
ALTER TABLE `login`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=63;

--
-- AUTO_INCREMENT de tabela `primeiro`
--
ALTER TABLE `primeiro`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=18;

--
-- AUTO_INCREMENT de tabela `segundo`
--
ALTER TABLE `segundo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=70;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
