#!/usr/bin/env python3

##################################################################
#
#   Phantasy Star Online Episode I&II for Gamecube Mag Hex Generator
#   written by Giuseppe Astrologo
#
#   For use with Item Creator 1.7 gamecube quest
#
#
#   Code works as follows (12 number hex code)
#   
#   X1 X2 X3 X4 D1 D2 E1 E2 F1 F2 G1 G2
#
#   X1 - 02 - Item type MAG
#   X2 - type of mag   
#   X3 - sum on stat levels, your mag
#   X4 - unkown
#   D1 - exp for def (if decimal value exceeds 256 then increment D2 and D1 starts back at 0)
#   D2 - number of 256 values overflowed on D1 ((d2 * 256)+d1) / 100 is your level for DEF
#   E1 & E2 like above but for POW
#   F1 & F2 like above but for DEX
#   G1 & G2 like above but for MIND
#
#
##################################################################


MAGS = [
    [['00', 'Mag'],       ['01', 'Varuna'],       ['02', 'Mitra']],
    [['03', 'Surya'],     ['04', 'Vayu'],         ['05', 'Varaha']],
    [['06', 'Kama'],      ['07', 'Ushasu'],       ['08', 'Apsaras']],
    [['09', 'Kumara'],    ['0A', 'Kaitabha'],     ['0B', 'Tapas']],
    [['0C', 'Bhirava'],   ['0D', 'Kalki'],        ['0E', 'Rudra']],
    [['0F', 'Marutah'],   ['10', 'Yaksa'],        ['11', 'Sita']],
    [['12', 'Garuda'],    ['13', 'Nandin'],       ['14', 'Ashvinau']],
    [['15', 'Ribhava'],   ['16', 'Soma'],         ['17', 'Ila']],
    [['18', 'Durga'],     ['19', 'Vritra'],       ['1A', 'Namuci']],
    [['1B', 'Sumba'],     ['1C', 'Naga'],         ['1D', 'Pitri']],
    [['1E', 'Kabanda'],   ['1F', 'Ravana'],       ['20',  'Marica']],
    [['21', 'Soniti'],    ['22', 'Preta'],        ['23',  'Andhaka']],
    [['24', 'Bana'],      ['25', 'Naraka'],       ['26',  'Madhu']],
    [['27', 'Churel'],    ['28', 'RoboChao'],     ['29',  'Opa-Opa']],
    [['2A', 'Pian'],      ['2B', 'Chao'],         ['2C',  'CHU CHU']],
    [['2D', 'KAPU KAPU'], ['2E', "ANGEL'S WING"], ['2F',  "DEVIL'S WING"]], 
    [['30', 'ELENOR'],    ['31', 'MARK3'],        ['32',  'MASTER SYSTEM']],
    [['33', 'GENESIS'],   ['34', 'SEGA SATURN'],  ['35',  'DREAMCAST']],
    [['36', 'HAMBURGER'], ['37', "PANZER'S TAIL"],['38',  "DEVIL'S TAIL"]],
    [['39', 'DEVA'],      ['3A', 'RATI'],         ['3B',  'SAVITRI']],
    [['3C', 'RUKMIN'],    ['3D', 'PUSHAN'],       ['3E',  'DIWARI']],
    [['3F', 'SATO'],      ['40', 'BHIMA'],        ['41',  'NIDRA']]
]


def to_hex(decimal):
    output = hex(decimal).split('x')[-1]
    if len(output) == 1:
        output = '0' + output

    return output


def level_to_hex_bytes(level):
  exp = level * 100
  byte_level = exp / 256
  byte_exp = exp % 256

  return to_hex(byte_exp), to_hex(int(byte_level))


def to_int(value, name):
    try:
        value = int(value)
    except ValueError as error:
        print("{0} value has to be an integer value.".format(name))
        return False
    return value


def print_table():
    for mag in MAGS:
        line = ''
        for value, name in mag:
            line += ' - '.join([value, name]).ljust(18)
            line += '|'
        print(line)


def check_mag_exists(hex_v):
    flatten = lambda l: [item for sublist in l for item in sublist]
    return any(hex_v in item for item in flatten(MAGS))


def main():
    print("What mag are you building?")
    print_table()

    while True:
        mag = input("Input hex value: ")
        if check_mag_exists(mag.upper()):
            break
        print("The hex value does not exist in the table")

    while True:
        def_lvl = input("Input DEF level: ")
        def_lvl = to_int(def_lvl, 'DEF')
        if def_lvl is not False:
            break

    while True:
        pow_lvl = input("Input POW level: ")
        pow_lvl = to_int(pow_lvl, 'POW')
        if pow_lvl is not False:
            break

    while True:
        dex_lvl = input("Input DEX level: ")
        dex_lvl = to_int(dex_lvl, 'DEX')
        if dex_lvl is not False:
            break

    while True:
        mind_lvl = input("Input MIND level: ")
        mind_lvl = to_int(mind_lvl, 'MIND')
        if mind_lvl is not False:
            break

    stat_list = [def_lvl, pow_lvl, dex_lvl, mind_lvl]
    levels = def_lvl + pow_lvl + dex_lvl + mind_lvl

    if levels > 200:
      print("Warning, level exceeds 200")

    bytes_list = ['02', mag, to_hex(levels), 'd9']
    for stat in stat_list:
        exp_byte, lvl_byte = level_to_hex_bytes(stat)
        bytes_list.append(exp_byte)
        bytes_list.append(lvl_byte)

    print("Item Code: {0} {1} {2}".format(bytes_list[0], bytes_list[1], bytes_list[2]))
    print("Parameters: {0} ".format(",".join(bytes_list[3:])))


if __name__ == '__main__':
    main()
