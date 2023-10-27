import random
import pickle

# Inisyalize varyab "scores" kom yon tach vid nan komansman an
scores = {}

# Fonksyon pou tcheke si yon epsedo valab (pa gen espas, ak nan piti)
def epsedo_valab(epsedo):
    return epsedo.islower() and ' ' not in epsedo

# Komanse jwet la
while True:
    print("Byenveni nan jwet Lawoulet!\nchwazi yon nimewo ant 0 ak 100")

    # Antre limit enferye nan enteval la
    while True:
        limit_enferye = int(input("Antre limit enferye nan enteval la : "))
        if 0 <= limit_enferye <= 100:
            break
        else:
            print("Tanpri antre yon nonm ant 0 ak 100.")

    # Antre limit siperye nan enteval la
    while True:
        limit_siperye = int(input("Antre limit siperye nan enteval la : "))
        if 0 <= limit_siperye <= 100:
            break
        else:
            print("Tanpri antre yon nonm ant 0 ak 100.")

    nimewo_sekre = random.randint(limit_enferye, limit_siperye)
    chans = 5  # Ou ka chanje kantite chans yo si ou vle

    epsedo = input("Antre yon epsedo (pa gen espas) : ").lower()

    if not epsedo_valab(epsedo):
        print("Epsedo pa valab. Asire ou pa gen espas nan li")
        continue

    if epsedo in scores:
        ansyen_sko = scores[epsedo]
    else:
        ansyen_sko = 0

    while chans > 0:
        devine = int(input(f"bonjou {epsedo} Devine yon nimewo ant {limit_enferye} ak {limit_siperye} : "))
        
        if devine < limit_enferye or devine > limit_siperye:
            print(f"{epsedo} Nimewo a dwe nan anteval {limit_enferye} ak {limit_siperye}.")
            continue

        if devine == nimewo_sekre:
            sko = chans * 30
            nouvo_sko = ansyen_sko + sko
            print(f"BRAVO {epsedo}! Ou jwenn nimewo a. Sko ou se {sko}. Sko total ou se {nouvo_sko}.")
            scores[epsedo] = nouvo_sko
            break
        elif devine < nimewo_sekre:
            print("Nimewo a pi wo.")
        else:
            print("Nimewo a pi ba.")
        
        chans -= 1
        print(f"{epsedo} Ou gen {chans} chans ki rete.")

    if chans == 0:
        print(f"Dezole {epsedo}, ou pedi. Nimewo a te {nimewo_sekre}.")

    jwe_anko = input("ou Vle jwe anko? (Peze 'K' pou sispann, oswa peze nenpot lot touch pou jwe anko) ")
    if jwe_anko.lower() == 'k':
        break


# Anrejistre baz done skò yo nan yon fichye
with open('sko.pkl', 'wb') as fichye:
    pickle.dump(scores, fichye)
