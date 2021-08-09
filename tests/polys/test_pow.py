"""
A pytest module to test modular exponentiation of polynomials over Galois fields.

Sage:
    to_coeffs = lambda poly: poly.coefficients(sparse=False)[::-1] if poly != 0 else [0]

    PARAMS = [(2,1), (2,8), (3,1), (3,5), (5,1), (5,4)]
    N = 20
    for p, m in PARAMS:
        print(f"POLY_POW_{p}_{m} = [")
        R = GF(p**m, repr="int")["x"]
        for _ in range(N):
            base = R.random_element(randint(0, 10))
            exponent = randint(0, 1000)
            modulus = R.random_element(randint(0, 10))
            result = base**exponent % modulus
            print(f"    ({to_coeffs(base)}, {exponent}, {to_coeffs(modulus)}, {to_coeffs(result)}),")
        print("]\n")
"""
import pytest

import galois

PARAMS = [(2,1), (2,8), (3,1), (3,5), (5,1), (5,4)]

# LUT items are (base(x), exponent, modulus(x), result(x)) all coefficients in degree-descending order

POLY_POW_2_1 = [
    ([1, 1, 1, 1, 0], 522, [1, 1, 1, 0, 0, 0, 0], [1, 1, 0, 0, 0, 0]),
    ([1, 1, 0, 1, 1, 0, 0, 0, 1, 1], 677, [1, 0], [1]),
    ([1, 1, 0, 0, 0], 203, [1, 1, 1, 1], [0]),
    ([1, 0, 0, 0, 0, 0, 1, 0], 697, [1], [0]),
    ([1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0], 152, [1, 1, 0, 0, 1, 0, 1], [1, 1, 1, 0, 0]),
    ([1, 1], 553, [1, 1, 0, 0, 0, 0, 1, 1], [1, 1, 1, 1, 0, 0]),
    ([1, 1, 0, 1, 0], 356, [1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 1], [1, 0, 1, 0, 0, 0, 1, 0, 0]),
    ([1, 0, 1, 0, 0, 0, 1, 1, 1, 0], 106, [1, 1, 0, 0, 1], [1, 1, 0, 0]),
    ([1, 1, 0, 0, 0], 976, [1, 1, 0, 0, 1, 0, 0, 1, 0, 1], [1, 0, 0, 0, 0, 0, 1, 1, 1]),
    ([1, 0, 0, 0, 0, 0, 0, 1, 0, 1], 528, [1, 0, 0, 1, 0, 0, 0, 0, 1, 1], [1, 1, 0, 1, 0, 0, 0]),
    ([1, 0], 956, [1, 0, 0, 1, 0, 0, 1, 1, 0], [1, 0, 0, 1, 0, 1, 0]),
    ([1, 1, 0, 1, 1, 0, 0, 1, 0, 0], 482, [1, 1], [1]),
    ([1, 0, 1, 1, 0, 1, 1, 0, 1], 177, [1, 0], [1]),
    ([1, 1, 1, 0, 1, 0], 529, [1, 1, 1, 1, 0, 1, 0, 0, 0, 1], [1, 1, 1, 1, 1, 1, 1, 1]),
    ([1, 1, 0, 1, 0, 0], 984, [1, 1, 0, 1, 1], [1]),
    ([1, 0, 1, 0, 0, 1, 0, 1, 1], 68, [1], [0]),
    ([1, 1, 0, 0, 1, 0], 198, [1, 0, 1, 0, 1, 1], [1, 1, 0, 0, 1]),
    ([1, 1, 0, 1, 1, 1, 0], 354, [1, 0], [0]),
    ([1, 1, 1, 1, 1, 0, 1, 1, 1, 0], 995, [1, 1, 1, 0, 1], [0]),
    ([1, 0, 0, 0, 1, 1, 0, 1, 1, 1], 795, [1, 1, 0], [1, 1]),
]

POLY_POW_2_8 = [
    ([174, 59, 0, 70, 249, 201, 71, 236, 93], 873, [123, 117, 163, 146, 118, 92, 156, 78], [46, 103, 154, 46, 30, 251, 54]),
    ([198, 244, 187, 8, 51, 12, 157, 228, 5, 245], 388, [220, 155, 66, 209], [69, 130, 168]),
    ([183, 86, 111, 128, 37, 148, 212, 98, 104], 489, [77, 246, 189, 12, 240, 205, 183, 213, 85, 62], [134, 62, 173, 162, 10, 21, 203, 60, 113]),
    ([209], 78, [120, 7], [161]),
    ([201, 4, 88, 171], 125, [207, 211, 102, 6, 214, 110, 189, 157, 31, 82], [41, 50, 189, 161, 13, 169, 77, 197, 210]),
    ([3], 625, [78, 12, 190, 244, 32, 136, 163, 248, 188], [94]),
    ([124, 175, 206, 244, 242, 240, 21, 187, 206, 14, 195], 759, [88, 11, 186, 74, 65, 7, 237, 75, 30], [9, 86, 73, 44, 0, 10, 183, 186]),
    ([178, 205, 13, 203, 190, 105, 120, 15, 69, 124, 59], 373, [173, 9, 30, 198, 168, 227, 120, 173], [184, 22, 39, 51, 87, 249, 40]),
    ([150, 6, 92, 157, 10, 24, 13, 201], 977, [83, 31, 94, 86, 102, 134], [6, 197, 64, 58, 252]),
    ([22, 24, 75, 195, 158, 176], 844, [211, 237, 9, 213, 89, 65, 103, 12, 255, 70, 89], [105, 44, 10, 195, 49, 237, 54, 97, 191, 197]),
    ([230, 74, 139, 139, 82, 84, 254, 137, 245, 26, 88], 864, [138, 48, 177], [207, 29]),
    ([60, 30, 85, 34, 148], 941, [189, 221, 173, 243, 243, 86, 34], [88, 18, 235, 184, 85, 79]),
    ([6], 473, [241, 60, 121, 89, 197], [105]),
    ([98, 86], 728, [96, 145, 71, 1, 174, 180, 55, 142, 93], [53, 26, 244, 200, 186, 60, 233, 166]),
    ([109, 32, 238, 19, 123, 213, 238, 41, 238, 82], 442, [228, 218, 236, 136], [202, 6, 54]),
    ([193, 175, 143, 232, 156, 95, 109, 96, 42], 369, [111, 240], [59]),
    ([21, 157, 179], 731, [148, 34], [214]),
    ([120, 209, 72, 166, 124, 128, 183, 252, 120, 140, 94], 733, [4, 143], [253]),
    ([159, 241, 42, 207], 879, [95], [0]),
    ([90, 132, 211, 16, 233, 142, 197, 253], 427, [64, 165, 93, 186, 13, 210, 124], [229, 124, 244, 177, 135, 59]),
]

POLY_POW_3_1 = [
    ([2, 2, 0, 1, 1, 0, 0, 2, 2, 2], 755, [1, 0, 1, 1, 0, 2, 0, 2, 0], [2, 0, 2, 0, 1, 0, 1, 2]),
    ([1], 761, [2, 1, 0, 2, 0, 0, 0, 0, 1, 0, 1], [1]),
    ([1, 2, 0, 1, 0, 2, 2, 0, 0, 2, 2], 380, [2, 0, 0, 1, 1, 2], [2, 1, 1, 0, 2]),
    ([1], 456, [1, 2, 2, 0, 2, 0, 2, 1], [1]),
    ([1, 1, 2, 0], 850, [1, 1, 2, 1], [1]),
    ([2, 2, 0, 0, 1, 0], 436, [1, 2], [1]),
    ([1, 1], 835, [2, 1, 2, 2, 2, 0, 1, 1, 0, 0], [1, 1, 2, 0, 1, 0, 1, 1]),
    ([2, 0, 0, 0, 1, 2, 2, 0], 592, [2, 0, 0, 1, 0, 2, 1, 1], [1, 0, 0, 0, 1, 2, 2]),
    ([2, 0, 1, 2, 0, 2, 2], 849, [1], [0]),
    ([2, 1, 0, 1, 1, 1, 1], 252, [2, 0, 1, 0, 2], [2]),
    ([2, 0, 2], 276, [2, 0, 1, 0, 2, 2, 0, 1], [2, 1, 2, 1, 2, 1]),
    ([1], 937, [1, 0, 2, 2, 2, 1], [1]),
    ([2], 914, [2, 2, 1, 2, 2, 0, 2, 0, 0, 0], [1]),
    ([1, 2, 0, 0, 2, 0, 0, 0, 0, 1, 2], 514, [1, 2, 1], [1]),
    ([1, 1, 0], 151, [1, 2, 2, 0, 2, 0, 2, 1, 2, 0], [1, 2, 2, 0, 0, 1, 1, 1, 0]),
    ([1, 1, 2], 185, [1, 1, 2, 1, 0, 2, 1, 2], [1, 2, 1, 0, 2, 2]),
    ([1, 2, 1, 2, 0, 2], 84, [1, 1, 2, 2, 1, 1, 2, 0, 0], [2, 2, 2, 1, 2, 0, 0, 1]),
    ([1, 1, 2, 2, 1, 0, 1, 0, 0, 2], 491, [1, 1, 1, 1, 0, 1, 1, 2, 1], [1, 1, 0, 1, 0, 1, 2, 1]),
    ([2, 1, 1, 1, 2, 1, 2, 1, 0, 2], 118, [1, 2, 0, 1, 0, 2, 1, 2], [1, 0, 0, 0, 0]),
    ([2, 2, 0, 2, 0, 1], 279, [1, 2, 1, 2, 0, 1, 0, 1, 1, 2, 2], [1, 0, 0, 1, 1, 1, 1, 1, 2, 2]),
]

POLY_POW_3_5 = [
    ([203, 167, 148, 10], 65, [148], [0]),
    ([211, 215, 117, 136, 234, 217], 850, [207, 29, 49, 151, 5, 55, 22, 84, 139, 32, 177], [179, 196, 23, 15, 11, 110, 96, 81, 38, 67]),
    ([111, 124, 225, 76, 232, 23], 307, [46], [0]),
    ([43, 56, 44], 364, [95, 21, 99, 153, 137, 82, 116, 120, 16, 174], [13, 144, 131, 35, 175, 210, 235, 226, 98]),
    ([57, 132, 114], 704, [215, 226, 228, 224, 221, 123, 223, 79], [66, 239, 96, 71, 241, 165, 17]),
    ([137, 133, 45, 8, 72, 5, 187], 764, [16, 85, 117, 33, 1, 228, 23, 136, 222, 144], [171, 185, 88, 61, 32, 190, 199, 47, 119]),
    ([228, 22, 62, 210, 127, 68, 17, 31], 517, [155, 213, 2, 206, 178, 102, 96, 75], [2, 53, 7, 233, 167, 206, 21]),
    ([55], 173, [238, 35, 211], [148]),
    ([135, 17, 10, 96, 128, 4, 182, 183, 8, 6, 159], 973, [105, 231], [200]),
    ([241, 191, 90], 763, [188, 102], [48]),
    ([180, 16], 815, [160, 56, 198, 235, 62, 133, 95, 191, 45], [197, 97, 51, 113, 51, 179, 126, 239]),
    ([14, 176, 151, 27, 77, 100, 237, 189], 114, [231, 136, 155, 175, 10, 155], [148, 14, 224, 165, 211]),
    ([14, 36, 143, 57, 6, 140, 75, 115], 953, [100, 148, 71], [228, 156]),
    ([66, 183, 224, 239, 11, 83, 121, 48, 38, 51], 888, [184, 237, 57], [2, 56]),
    ([160, 69, 64, 58, 3], 15, [67, 80, 152, 9, 176, 100, 62, 198, 54], [229, 1, 81, 220, 162, 133, 0, 237]),
    ([90], 601, [121, 119, 228, 95, 58, 224, 52], [96]),
    ([169, 39, 125, 224, 121, 195, 116], 355, [3, 32, 157, 31, 168, 46, 43], [34, 7, 65, 221, 134, 37]),
    ([142, 35, 160, 73, 183, 163, 241, 106, 108, 182, 21], 761, [183, 51], [170]),
    ([225, 54, 88, 59, 44, 27], 630, [190, 48], [241]),
    ([120], 299, [139], [0]),
]

POLY_POW_5_1 = [
    ([4, 4, 3, 0, 0, 3], 627, [4, 4], [0]),
    ([2, 1, 4, 4, 0], 487, [1, 2, 0, 2, 3, 3, 1], [4, 3, 3, 4, 2, 4]),
    ([2, 3, 3, 1, 0], 662, [1, 3, 3, 3, 4, 2, 3, 3, 0], [3, 1, 4, 3, 2, 4, 3, 0]),
    ([1, 4, 2, 2], 815, [3, 1, 1, 3], [4, 3, 1]),
    ([1, 0, 4, 4, 1, 2, 1, 0, 4, 3, 1], 993, [4], [0]),
    ([4, 4, 1], 813, [2, 2, 1, 1], [1, 0, 0]),
    ([4, 2, 2, 2], 126, [1, 1, 3, 0, 1, 1, 3, 4, 3, 4, 4], [2, 2, 1, 1, 1, 2, 4, 0, 0, 2]),
    ([3, 1, 0, 3, 0, 0, 3, 3], 339, [1, 0, 2, 3, 3, 3, 2, 4, 4], [4, 2, 0, 1, 4, 4]),
    ([4, 1, 2, 3, 2, 1], 973, [2, 0, 4, 0, 1, 0, 1, 1, 1], [1, 1, 2, 0, 1, 4, 2, 2]),
    ([3, 2, 4, 2, 3, 4, 0, 1, 4], 682, [4, 0, 1, 2, 0, 1, 3, 0, 0], [1, 4, 3, 2, 4, 4, 3, 1]),
    ([2], 818, [1, 0, 0, 3], [4]),
    ([1, 0, 4, 2, 0, 4], 890, [2, 1], [1]),
    ([1, 2, 0, 3, 3, 3, 2, 4, 2, 4, 1], 179, [4, 3, 0, 2, 1, 1, 4], [1, 1, 3, 1, 2, 2]),
    ([4, 2, 2, 2, 2], 573, [1, 4, 0, 2, 3, 0], [4, 2, 2, 2, 2]),
    ([4, 4, 2, 2], 309, [1, 3, 3, 1, 4], [1, 4, 2, 2]),
    ([3, 4, 1], 424, [4, 3, 1, 0, 2], [3, 4, 4]),
    ([1, 1, 2, 2, 2, 2, 4, 2, 0], 852, [4, 2, 3, 3], [0]),
    ([1, 0, 1, 4, 1, 3], 978, [1, 3, 1], [0]),
    ([1, 1, 0, 2, 3, 2, 2, 1, 3, 2], 100, [1, 3, 4, 4, 1, 2], [1, 4, 1, 4, 1]),
    ([4], 303, [2, 4, 0, 1, 2, 1, 1, 4], [4]),
]

POLY_POW_5_4 = [
    ([17, 478, 199], 444, [334, 146, 158, 79, 363, 561, 555, 176], [516, 108, 517, 264, 479, 538, 262]),
    ([587, 603, 469], 54, [193, 510], [260]),
    ([273, 512, 572, 360, 423, 301], 15, [599, 55, 206], [457, 134]),
    ([192, 431, 270, 539, 6, 427, 92], 971, [343, 206, 404, 125, 484, 226, 145, 106, 386], [54, 347, 418, 333, 393, 493, 381, 312]),
    ([475, 196, 577, 470, 513, 99], 582, [388, 242, 45, 66, 107, 237, 209, 7, 1], [313, 375, 48, 490, 561, 527, 22, 435]),
    ([81, 34], 889, [354, 1, 473, 213, 484, 503, 361, 12, 410, 224], [523, 98, 33, 608, 560, 198, 41, 123, 587]),
    ([295, 113, 311, 106, 166, 543], 722, [367, 244, 315, 573, 177], [349, 101, 473, 462]),
    ([277, 317, 7, 372, 144, 209, 236, 476, 377, 476], 245, [551, 198, 388, 287, 107], [549, 203, 512, 199]),
    ([10, 370, 180, 581, 172, 463, 497, 569, 270], 752, [313, 4, 40, 137], [244, 24, 157]),
    ([337, 594], 485, [409], [0]),
    ([84], 363, [45, 352, 57, 511, 617, 616, 587, 185], [79]),
    ([22, 567, 604, 98, 7, 173, 139, 436], 394, [256, 360, 540], [570, 297]),
    ([153, 510, 383], 100, [533, 58, 296, 207], [180, 341, 389]),
    ([421, 428, 528, 346, 209], 147, [409, 597, 257, 14, 478, 70], [180, 457, 106, 181, 540]),
    ([40, 43, 479, 611, 314, 85, 239], 672, [601, 105, 595, 379, 314, 38, 370, 549, 180, 379], [189, 538, 515, 436, 618, 126, 427, 207, 109]),
    ([447, 602, 39, 601, 126, 509, 188, 614, 285], 638, [595, 624, 298, 189, 397, 248, 519, 232, 5], [260, 367, 275, 600, 458, 125, 232, 550]),
    ([168, 308, 374], 175, [415, 8, 580, 74], [461, 220, 422]),
    ([356, 9, 56, 164, 479, 579], 470, [396, 572, 134, 211], [117, 413, 409]),
    ([581, 620, 433, 52], 612, [84, 0, 200, 269, 304, 570, 378, 525, 394], [522, 213, 436, 90, 112, 331, 536, 499]),
    ([592, 115, 548, 327, 157, 414, 138, 243, 293], 756, [150, 267, 571, 195, 471, 101], [374, 327, 607, 156, 409]),
]


def test_poly_pow_exceptions():
    GF = galois.GF(31)
    f = galois.Poly.Random(10, field=GF)
    g = galois.Poly.Random(7, field=GF)
    power = 20

    with pytest.raises(TypeError):
        galois.poly_pow(f.coeffs, power, g)
    with pytest.raises(TypeError):
        galois.poly_pow(f, float(power), g)
    with pytest.raises(TypeError):
        galois.poly_pow(f, power, g.coeffs)
    with pytest.raises(ValueError):
        galois.poly_pow(f, -power, g)


@pytest.mark.parametrize("characteristic,degree", PARAMS)
def test_poly_pow(characteristic, degree):
    GF = galois.GF(characteristic**degree)
    LUT = eval(f"POLY_POW_{characteristic}_{degree}")
    for item in LUT:
        base = galois.Poly(item[0], field=GF)
        exponent = item[1]
        modulus = galois.Poly(item[2], field=GF)
        result = galois.Poly(item[3], field=GF)
        assert galois.poly_pow(base, exponent, modulus) == result
