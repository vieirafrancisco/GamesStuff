# Pokémon tile-based game
A game based on [PxG](https://www.pokexgames.com/#/home) game style!

## ToDo stuff

### Enemy:
- [x] random walk movement
- [x] respawn position
- [x] limit walk range (square walk space)
- [x] collision with other entities and map tiles
- [x] player collision with enemies (change entities position in the map class)
- [x] add probability of choice movement, look at the four positions and verify collision to calculate probablility
- [ ] smooth movement

### Animation:
- [ ] create logic to animation
- [ ] create player animation

### Refactoring code:
- [x] create camera class to render the images in the screen (tiles and entities)
- [x] unify tiles and entities to entities objects
- [x] instead of tiles and entities lists, create a stack of entities idexed by the tile position in the map
- [x] refactor entity collision verification based on the top entity in the stack in the map