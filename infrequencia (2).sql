-- phpMyAdmin SQL Dump
-- version 5.2.1
-- https://www.phpmyadmin.net/
--
-- Host: 127.0.0.1
-- Tempo de geração: 17/06/2023 às 22:52
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
(39, 'ddddd', 'ddd', 'Professor', 'eeeee');

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
(55, 'Lara', '2023-06-10 18:22'),
(56, 'Lara', '2023-06-10 18:22'),
(57, 'luiza', '2023-06-11 20:16'),
(58, 'Caua', '2023-06-11 20:27'),
(59, 'lara', '2023-06-11 20:27'),
(60, 'luiza', '2023-06-11 20:29'),
(61, 'lara', '2023-06-17 15:51'),
(62, 'lara', '2023-06-17 16:03'),
(63, 'Lara', '2023-06-17 16:10');

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
  `data` varchar(36) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `primeiro`
--

INSERT INTO `primeiro` (`id`, `numero`, `nome`, `horario`, `serie`, `data`) VALUES
(7, '08', 'Antonio Caua de Brito Augusto Sales', '6º', '1º', NULL),
(8, '05', 'Arthur Rocha da Silva Alves', '2º', '1º', NULL),
(9, '06', 'Ana Beatriz Pereira Martins', '3º', '1º', NULL),
(10, '10', 'Caio Lucas Moreno Vieira', '6º', '1º', NULL),
(11, '08', 'Caio Lucas Moreno Vieira', '3º', '1º', NULL),
(12, '44', 'Pedro Henrique de Oliveira Carvalho', '6º', '1º', NULL),
(13, '33', 'Laís de Sena Oliveira', '9º', '1º', NULL),
(14, '28', 'Átila do Nascimento Rocha', '6º', '1º', NULL),
(15, '06', 'Diogo Yuri dos Santos Rodrigues', '5º', '1º', '2023-06-17 16:51:09.798380'),
(16, '09', 'Francisco Aluisio dos Santos Clemente', '5º', '1º', '2023-06-17 17:24:20.468267');

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
  `data` varchar(36) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `segundo`
--

INSERT INTO `segundo` (`id`, `numero`, `nome`, `horario`, `serie`, `data`) VALUES
(2, '05', 'Ana Luiza Bezerra de Freitas', '4º', '2º', NULL),
(3, '09', 'Daniel Bezerra Silva Filho', '9º', '2º', NULL),
(4, '08', 'Eloisa Braga Farias', '7º', '2º', NULL),
(5, '09', 'Daniel Bezerra Silva Filho', '3º', '2º', NULL),
(6, '02', 'Antonia Vladia de Sousa Moreira', '2º', '2º', NULL),
(7, '01', 'Adriel Levi de Sousa Vieira', '1º', '2º', NULL),
(8, '04', 'Antonia Vladia de Sousa Moreira', '5º', '2º', NULL),
(9, '03', 'Antonia Vladia de Sousa Moreira', '6º', '2º', NULL),
(10, '05', 'Daniel Bezerra Silva Filho', '9º', '2º', '2023-06-17 16:50:40.122853'),
(11, '06', 'Cleber Lucas da Costa Macedo', '5º', '2º', '2023-06-17 17:25:28.540462'),
(12, '10', 'Antonio Anderson Faustino Andre', '9º', '2º', '2023-06-17 17:25:37.804794');

-- --------------------------------------------------------

--
-- Estrutura para tabela `terceiro`
--

CREATE TABLE `terceiro` (
  `id` int(11) NOT NULL,
  `numero` varchar(10) NOT NULL,
  `nome` varchar(150) NOT NULL,
  `horario` varchar(30) NOT NULL,
  `serie` varchar(10) NOT NULL,
  `data` varchar(36) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_general_ci;

--
-- Despejando dados para a tabela `terceiro`
--

INSERT INTO `terceiro` (`id`, `numero`, `nome`, `horario`, `serie`, `data`) VALUES
(54, '04', 'Angelo Gabriel Vieira de Oliveira', '2º', '3º', NULL),
(56, '05', 'Angelo Gabriel Vieira de Oliveira', '3º', '3º', NULL),
(57, '05', 'Bruno Henrique do Nascimento Firmino', '3º', '3º', NULL),
(65, '05', 'Bruno Henrique do Nascimento Firmino', '7º', '3º', NULL),
(66, '06', 'Cauã Roberto de Souza', '3º', '3º', NULL),
(73, '04', 'Angelo Gabriel Vieira de Oliveira', '4º', '3º', NULL),
(77, '02', 'Bruno Henrique do Nascimento Firmino', '4º', '3º', NULL),
(78, '03', 'Bruno Henrique do Nascimento Firmino', '4º', '3º', NULL),
(81, '03', 'Ashley Darwin de Souza Duarte', '4º', '3º', NULL),
(82, '03', 'Lara Evelyn de Sousa Pinto', '3º', '3º', NULL),
(83, '10', 'Eric do Nascimento Sousa Diniz', '9º', '3º', NULL),
(84, '10', 'Emanoell Edvan Souza da Silva', '4º', '3º', NULL),
(85, '10', 'Cauã Roberto de Souza', '8º', '3º', NULL),
(88, '06', 'Andressa da Silva Matos', '1º', '3º', NULL),
(89, '06', 'Bruno Henrique do Nascimento Firmino', '4º', '3º', NULL),
(90, '05', 'Maria Eduarda Castro dos Santos', '6º', '3º', NULL),
(91, '05', 'Luana Hevillyn Morais da Silva', '6º', '3º', NULL),
(92, '03', 'Bruno Henrique do Nascimento Firmino', '3º', '3º', NULL),
(93, '05', 'Ashley Darwin de Souza Duarte', '5º', '3º', NULL),
(94, '05', 'Cauã Roberto de Souza', '4º', '3º', NULL),
(95, '06', 'Angelo Gabriel Vieira de Oliveira', '6º', '3º', NULL),
(96, '06', 'Cauã Roberto de Souza', '8º', '3º', NULL),
(97, '04', 'Bruno Henrique do Nascimento Firmino', '4º', '3º', NULL),
(98, '04', 'Angelo Gabriel Vieira de Oliveira', '6º', '3º', NULL),
(99, '01', 'Aila Vitória Braga da Silva', '1º', '3º', NULL),
(100, '04', 'Angelo Gabriel Vieira de Oliveira', '1º', '3º', '2023-06-17 17:00:04.917334');

--
-- Índices para tabelas despejadas
--

--
-- Índices de tabela `cadastro`
--
ALTER TABLE `cadastro`
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
-- Índices de tabela `terceiro`
--
ALTER TABLE `terceiro`
  ADD PRIMARY KEY (`id`);

--
-- AUTO_INCREMENT para tabelas despejadas
--

--
-- AUTO_INCREMENT de tabela `cadastro`
--
ALTER TABLE `cadastro`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=40;

--
-- AUTO_INCREMENT de tabela `login`
--
ALTER TABLE `login`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=64;

--
-- AUTO_INCREMENT de tabela `primeiro`
--
ALTER TABLE `primeiro`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=17;

--
-- AUTO_INCREMENT de tabela `segundo`
--
ALTER TABLE `segundo`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=13;

--
-- AUTO_INCREMENT de tabela `terceiro`
--
ALTER TABLE `terceiro`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=101;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
