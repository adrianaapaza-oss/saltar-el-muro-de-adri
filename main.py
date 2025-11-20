scene.set_background_color(3)
tiles.set_current_tilemap(tilemap("""
    nivel1
    """))
info.set_life(5)
PERSONAJE = sprites.create(img("""
        . . . . f f f f . . . . .
        . . f f f f f f f f . . .
        . f f f f f f c f f f . .
        f f f f f f c c f f f c .
        f f f c f f f f f f f c .
        c c c f f f e e f f c c .
        f f f f f e e f f c c f .
        f f f b f e e f b f f f .
        . f 4 1 f 4 4 f 1 4 f . .
        . f e 4 4 4 4 4 4 e f . .
        . f f f e e e e f f f . .
        f e f b 7 7 7 7 b f e f .
        e 4 f 7 7 7 7 7 7 f 4 e .
        e e f 6 6 6 6 6 6 f e e .
        . . . f f f f f f . . . .
        . . . f f . . f f . . . .
        """),
    SpriteKind.player)
controller.move_sprite(PERSONAJE, 100, 0)
PERSONAJE.ay = 600
scene.camera_follow_sprite(PERSONAJE)
tiles.place_on_random_tile(PERSONAJE, assets.tile("""
    transparency16
    """))
ENEMIGO = sprites.create(img("""
        . . . . . c c c c c c c . . . .
        . . . . c 6 7 7 7 7 7 6 c . . .
        . . . c 7 c 6 6 6 6 c 7 6 c . .
        . . c 6 7 6 f 6 6 f 6 7 7 c . .
        . . c 7 7 7 7 7 7 7 7 7 7 c . .
        . . f 7 8 1 f f 1 6 7 7 7 f . .
        . . f 6 f 1 f f 1 f 7 7 7 f . .
        . . . f f 2 2 2 2 f 7 7 6 f . .
        . . c c f 2 2 2 2 7 7 6 f c . .
        . c 7 7 7 7 7 7 7 7 c c 7 7 c .
        c 7 1 1 1 7 7 7 7 f c 6 7 7 7 c
        f 1 1 1 1 1 7 6 f c c 6 6 6 c c
        f 1 1 1 1 1 1 6 6 c 6 6 6 c . .
        f 6 1 1 1 1 1 6 6 6 6 6 6 c . .
        . f 6 1 1 1 1 1 6 6 6 6 c . . .
        . . f f c c c c c c c c . . . .
        """),
    SpriteKind.enemy)
tiles.place_on_random_tile(ENEMIGO, assets.tile("""
    transparency16
    """))
ENEMIGO.follow(PERSONAJE, 80)
info.start_countdown(60)