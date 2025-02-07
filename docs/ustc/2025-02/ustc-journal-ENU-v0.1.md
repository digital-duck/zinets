---
documentclass: article
CJKmainfont: "Noto Sans CJK SC"
geometry: margin=1in
---

# A New Exploration into Chinese characters: from Simplification to Deeper Understanding

## Motivation

Learning 汉字 (Hànzì) and, by extension, the Chinese language presents a unique and substantial challenge for learners, particularly those whose native languages utilize alphabetic systems. The difficulty stems primarily from the logographic nature of 汉字, where each character represents a morpheme (or word) rather than a sound. Unlike phonetic scripts, there's often no readily apparent connection between a character's visual form and its pronunciation, demanding rote memorization of thousands of distinct characters to achieve basic literacy. This is compounded by the tonal nature of Mandarin Chinese, where changes in pitch can drastically alter the meaning of a word, adding another layer of complexity. Furthermore, the sheer volume of characters, the subtle nuances in stroke order and character composition, and the existence of both traditional and simplified forms, require a sustained and dedicated learning effort over a prolonged period, making the acquisition of fluency in written and spoken Chinese a significantly time-intensive undertaking compared to many other languages.

Inspired by the success of reductionism in science, such as the discovery of fundamental particles in physics and the organization of the periodic table in chemistry, this research seeks to apply similar principles to the learning of 汉字. This involves three key approaches:

- **Network Analysis**: Leveraging computer science and network analysis techniques, this study aims to uncover the hidden relationships and underlying structures within the large collection of Chinese characters. By mapping these connections, the research hopes to reveal patterns and simplify the seemingly chaotic complexity of the character system.

- **Artificial Intelligence (AI) Assistance**: Recognizing the burden of rote memorization in traditional 汉字 learning, this research explores the use of AI to alleviate this challenge. The goal is to develop AI-powered tools that can assist learners in memorizing the form, pronunciation, and meaning of characters, as well as their complex interactions and contextual usage.

- **Improve learning and learning expeirence**: The overarching research goal, built upon by applying network analysis and AI asisstance, is to reduce the learning burdens for students and enrich their learning experiences.


By combining these computational and AI-driven approaches with a reductionist perspective, the research aims to provide a novel exploration into understanding and learning 汉字, ultimately making the process more efficient, intuitive, and enjoyable for learners.


## ZiNets: Computational Network Analysis on Chinese Characters


The foundational work Shuowen Jiezi (《说文解字》), compiled by Xu Shen (许慎) during the Eastern Han Dynasty, represents the first systematic attempt to analyze the structure and etymology of Chinese characters [r_zi, r_xushen, r_sears]. Xu Shen identified 540 radicals (部首, bùshǒu) and used his "six scripts" (六书, liùshū) theory to explain character formation, categorizing characters based on their composition: pictographs (象形), ideographs (指事), compound ideographs (会意), phono-semantic compounds (形声), and two less-common categories (转注 and 假借). While groundbreaking, the Shuowen Jiezi's analysis, focused on the Small Seal Script (小篆), doesn't perfectly reflect the modern forms of many characters, and its 540 radicals, while valuable, do not always represent the smallest, irreducible components. 

The later Zihui dictionary and the Kangxi Dictionary (康熙字典) refined and reduced this system, ultimately settling on the 214 Kangxi radicals [r_kangxi], which serve as a standard indexing system. These radicals, based primarily on shared visual components, often relating to meaning (semantic radicals, or 形旁, xíngpáng), provide a method for dictionary lookups. While many radicals also hint at pronunciation (phonetic radicals, or 声旁, shēngpáng), this is not always reliable. The Kangxi system, though widely used, has limitations: ambiguous categorization, inconsistent semantic and phonetic roles, and some radicals that, due to their complexity or low frequency of occurrence, are not always the most informative units for understanding character structure. 

Building upon the legacy of Xu Shen and Kangxi systems, the author has developed a web application called "ZiNets".
With this tool and computational network structure, we decomposed 6190 chinese characters [r_mdbg] (including 3910 HSK common characters [r_hsk]). Elemental characters were identified as those components appearing with a frequency above a defined threshold.

To systematically analyze the structure of Chinese characters, we introduce a novel spatial decomposition model, the "Zi Matrix." This model represents each character as a matrix of up to eleven distinct positional components. These positions are defined as: Top (上), Bottom (下), Left (左), Right (右), Center (中), Top-Left (左上), Top-Right (右上), Bottom-Left (左下), Bottom-Right (右下), Center-Inside (中内), and Center-Outside (中外). Each position within the matrix can be either occupied by a specific character component (a radical, a stroke, or a more complex sub-component) or remain empty. This 11-component matrix allows for a consistent and structured representation of the spatial relationships between the constituent parts of any Chinese character, regardless of its complexity.

![zi-matrix-CHN](./images/zi-matrix-CHN.png)

The decomposition of each character into the Zi Matrix is performed manually using a hierarchical approach. This process involves a series of decomposition steps. First, the character is broken down into its major components, assigning each to its appropriate position within the matrix. If a component itself is complex, it is further decomposed, recursively, into its constituent parts, again assigning them to positions within a sub-matrix representing that component. This hierarchical decomposition continues until the most fundamental components – those that cannot be reasonably further divided – are identified. These fundamental components become candidates for the "elemental character" set. This manual, hierarchical approach ensures a consistent and considered analysis of character structure, leveraging expert linguistic knowledge to guide the decomposition.

![zi-matrix-CHN](./images/app_decomposing-zi.png)

## Elemental Characters Analysis




## Storytelling Characters

## Natural Evolution of Characters

## Conclusion


## Dedication

This work is dedicated to late Professor T.D. Lee（李政道）, whose pioneering efforts opened doors for many Chinese students to pursue studies and research in the United States, fostering a bridge between Eastern and Western scientific traditions. His vision and support have enabled countless scholars like myself to contribute to global scientific discourse.

This work is also dedicated to author's parents (龚永权，文国芳), who nurtured his intellectual curiosity through hardships and challenging times. Their sacrifices and unwavering support are forever remembered.

## Acknowledgements

This paper represents a collaborative effort between the author, and a team of AI assistants (Claude 3.5 from Anthropic, Gemini 2 from Google, Qwen2.5-Max from Alibaba, and DeepSeek V3 from DeepSeek). The fusion of human knowledge and insight in software development, physics, and Chinese language with AI's analytical capabilities enabled the development of the novel perspectives and methodologies presented in this work. This collaboration demonstrates the potential of human-AI partnerships in research and learning, particularly in interdisciplinary studies bridging traditional knowledge with modern computational technologies.


## References

[r_zi] https://www.wikiwand.com/en/articles/Chinese_characters

[r_xushen] 說文解字 : https://www.shuowen.org/

[r_kangxi] Kangxi radicals : https://en.wikipedia.org/wiki/Kangxi_radicals

[r_sears] Sears, Richard. Chinese Etymology research website at https://hanziyuan.net/

[r_mdbg] CC-CEDICT dictionary dataset : https://www.mdbg.net/chinese/dictionary?page=cc-cedict

[r_hsk] 书同文 汉字网 HSK 汉语水平考试汉字列表 : https://hanzi.unihan.com.cn/School/HSK

[r_chaizi] 漢語拆字字典 : https://github.com/kfcd/chaizi

[r_google_img] Google ImageFx text-to-image generation tool: https://labs.google/fx/tools/image-fx

[r_qwen] Qwen2.5-MAX text-to-image generation tool: https://chat.qwenlm.ai/

[r_fibonacci] https://www.wikiwand.com/en/articles/Fibonacci_sequence



## Appendix


# =============================================================
# Outline
**Title:** "Hanzi: A New Exploration, from Simplification to Deeper Understanding" (This is a more idiomatic translation of your title)



**Abstract:** (We'll write this last, after the main body is complete)



**1. Introduction (缘起 - Motivation):**

    * Briefly introduce the challenge of learning Hanzi. (Use the paragraph we already worked on).

    * Highlight the limitations of traditional rote memorization methods.

    * Introduce the core idea: Applying a reductionist approach inspired by physics (fundamental particles, periodic table).

    * State the goals:

        * Simplify the learning process using network analysis (ZiNets) and AI.

        * Deepen understanding of character meaning and etymology.

        * Present three key areas of exploration: elemental character identification, pattern analysis, and character etymology ("storytelling").

        * Mention anniversary reason



**2. ZiNets and Elemental Character Identification (汉字网络 ZiNets 与元字):**

    * **2.1 Methodology:**

        * Explain the ZiNets software and its functionality.

        * Describe the data source (HSK 3000 characters).

        * Define "elemental character" (元字) – your operational definition. This is *crucial*. Are these the smallest indivisible units, or are they characters that frequently act as components? Are they purely *structural* components, or do they also need to have a consistent semantic or phonetic role?

        * Detail the algorithm used to decompose characters and identify elemental characters. Be very specific here.

    * **2.2 Results:**

        * Present the list of identified elemental characters (元字).

        * Provide statistics: How many elemental characters were found?

        * Visualize the network (a key figure). Show a sample of the network, highlighting elemental characters.



**3. Elemental Character Analysis (元字概念与频率):**

    * **3.1 Categorization:**

        * Classify elemental characters into categories: form radicals (形旁), phonetic radicals (声旁), and semantic radicals (义旁, also consider if some are purely structural and don't fit neatly into these traditional categories).

        * Explain the criteria used for this classification.

    * **3.2 Frequency Analysis:**

        * Present the frequency distribution of elemental characters. Which are the most common?

        * Compare the frequency of elemental characters to the overall frequency of characters in the HSK 3000.

        * Visualize this data (e.g., a bar chart or table).

    * **3.3 Combination rules:**

    * Present statistics of different combination patterns

    * Visualize this data (e.g., a bar chart or table).



**4. Character Etymology and "Storytelling" (汉字故事):**

    * **4.1 Methodology:**

        * Explain your approach to reconstructing character etymologies. Are you using existing etymological dictionaries (like 說文解字), or are you deriving etymologies from the ZiNets analysis? This is important to clarify.

        * Explain how AI is used (if at all) in this section. Is it used for generating stories, or for analyzing etymological data? Be precise.

    * **4.2 Examples:**

        * Present detailed etymological analyses of several key characters (日, 禺, 乍, 寺, 子, and others). Show how they are built from elemental characters.

        * Use these examples to illustrate the principles of character formation.

        * Show how understanding the etymology can aid memorization and comprehension.

        * Explain 诗: temple of words



**5. Natural Evolution of Characters (文字自然演化):**

    * **5.1 Fibonacci Sequence Pattern:**

        * Explain the connection you've found between character structure/formation and the Fibonacci sequence. This needs a strong, clear explanation with visual examples. What aspect of characters exhibits this pattern? Is it the number of strokes, the number of components, the frequency of certain combinations?

        * Provide statistical evidence to support your claim.

        * Discuss the implications of this finding. Does it suggest an underlying principle of efficiency or aesthetics in character evolution?



**6. Conclusion (结语):**

    * Summarize the key findings of the research.

    * Reiterate the benefits of the ZiNets approach and the use of AI for learning Hanzi.

    * Suggest future research directions.

    * Mention 40th year since graudation