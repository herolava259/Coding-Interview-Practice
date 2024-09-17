from typing import List


class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        weights: List[int] = [len(word) + 1 for word in words]
        total_line: List[int] = []
        offset: int = 0

        curr_idx = 0
        n = len(words)
        end_idxs: List[int] = []
        while curr_idx < n:
            len_line = weights[curr_idx]
            while curr_idx + 1 < n and len_line + weights[curr_idx + 1] <= maxWidth + 1:
                curr_idx += 1
                len_line += weights[curr_idx]
            if curr_idx + 1 == n:
                end_idxs.append(curr_idx)
                total_line.append(len_line)
                break
            total_line.append(len_line)
            end_idxs.append(curr_idx)
            curr_idx += 1
        res: List[str] = []
        srt_idx = 0
        for end_idx, len_char in zip(end_idxs[:-1], total_line[:-1]):
            num_space = end_idx - srt_idx
            line = ''
            if num_space == 0:
                line += words[end_idx] + ' ' * (maxWidth - weights[end_idx] + 1)
                res.append(line)
                srt_idx = end_idx + 1
                continue

            remain_bp = maxWidth - len_char + 1
            unit_bp = remain_bp // num_space
            residual_bp = (remain_bp % num_space)
            remain_bp -= residual_bp

            for i in range(srt_idx, end_idx):
                len_bp = min(unit_bp, remain_bp)
                resi = 0
                if residual_bp > 0:
                    resi = 1
                    residual_bp -= 1
                line += words[i] + ' ' * (len_bp + 1 + resi)
                remain_bp -= len_bp
            line += words[end_idx]
            res.append(line)
            srt_idx = end_idx + 1
        end_idx, len_char = end_idxs[-1], total_line[-1]
        num_space = end_idx - srt_idx + 1
        line = ''
        if num_space == 0:
            line += words[end_idx] + ' ' * (maxWidth - weights[end_idx] + 1)
            res.append(line)
            return res
        remain_bp = maxWidth
        for i in range(srt_idx, end_idx + 1):
            remain_bp -= len(words[i])

            bp_num = min(1, remain_bp)
            line += words[i] + ' ' * bp_num
            remain_bp -= bp_num
        line += ' ' * remain_bp
        res.append(line)
        return res

words_inp = ["ask","not","what","your","country","can","do","for","you","ask","what","you","can","do","for","your","country"]

max_width = 16
print(Solution().fullJustify(words_inp, max_width))