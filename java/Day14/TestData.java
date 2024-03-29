public class TestData {

    public static String SMALL_MAP = 
        """
        O....#....
        O.OO#....#
        .....##...
        OO.#O....O
        .O.....O#.
        O.#..O.#.#
        ..O..#O..O
        .......O..
        #....###..
        #OO..#....
        """;

    public static String FULL_MAP = """
        #...#..O#.OO...#......#...O.#.O#.O........O#..O#.O.OO..O.......O....##..O#O.........#O....O..O#.....
        OO..O....#.####...#.O..#.....OO.O...O.#OOO.##..O.#.OO.#....O.#....#..#.O#..O#.O...#OO.#....#.O.#...O
        ..........O..#..OO.O...##.O........O#O#.#...#O....O.........O.....OO#....O..............#......#...#
        #..O.O.#OO#....O#OO.#.#.O..O#...#.OO#.O#.O......#.....OO...O#.O....O..#.O#..#..O.#.O........#..#..O#
        ...#..O#.OO..#O...#..#..O###.........#.....OOOOOO.........#O.O.O#O.O.......O........#.OO....O..#...O
        ..OO...O.#.......#.#O....#..O##....O.O..OOO...#O.#..O.#O...#.O..O..#O#.#OO...O.OO..#..O..O.O.O....O#
        .OO#............O.O...#.OO.#..##O......OO...#......##......#.#..#.O..O.O...#..#...O#......O..OOO....
        ..........O..#O...O.#....OOO.#........#.##O.#......#..###O...O...O..O.#.O..O.#..O.O.O.O.##.....#.#..
        .##.O#O.........O.#.OOOO..O..O#.#..O.O...O..#......O.O.#O........O..#.#..#OO...#......##O.#O..O.OO..
        .O.O.O##...O...O.........O##O##....#O....O#...OO.O.#..#O....OO...O.O.....##.....#..O#O#.#...O..O..#.
        ..OO#.#O.#...............#...#.#.O..#..O.#.#..O.##O..OOO..#O#....##.#.#...#.#.O#.#.O..#.#......#....
        .#...#.#....O..O.#..O.O..O.....##O#..#.##..OO.....OO.OO..OO...O#...O.O...O.OO##.....O..............O
        .....O.....#........#O..#.OO#..O...#O....OO..O.#.OOO.#O.O......#O.#.....#O..O..O#..#.#.#.O..O.#...OO
        #.....#..OO.#....#.##.O.##..O.#.O#.O...O...#O.#.O#..O.#...##....OO#OO......#.O...O.O#.#...O...##.OO#
        O.......O......O..O...#...#..#...##.##..O...O....O.##.#.#OO#.....#.O#...O.##O...O..........#..##.O.O
        ..............OO.O##.....#.O......##O#....O.O....O..##.#.............O#...O.#OO...O....#...O..O#..OO
        .#O#...OO...#.#.....O#...O#.O.O#..O..##O.#.#..OO.O.##.#......O..O.O.O...#......OO#.#.#.#.O.OOO#.O.O.
        ..#...#..O.........O.O.O..O.........#..#....#.O#..#O...............O##.O##O.O..O#.#....O.#OO.#.#....
        ..#.#OO.OO..OO#..#O..O##.....O......OO..O.#..O#.......O..##..##.O.O..O.#O....O.O.......O....O....#.#
        ....OOOOO.#.#......#.........#.O.O....O....#.O..O#.....O##..........#..#.....O..O.....O....O.#O.#...
        OOO.O#..#...O#...O.#..OOO.#.....O..#.O#.O.O.O.#O..#...#...#O....O.#..O..#O..O.#O#.OOOO..............
        .#.O#OO#..##...O.#..O.O....#O........#O.....O..O....O.....#...#O.O..........#.......OO#...O..OO.##.O
        OO.....O#.O....O..O.O.#.#O#.......#..##...O.......O...OOO...#...#OO.OO#....O#........OO.OO..OO....##
        ..O..#..#.#.O..O...#.#.#.O......O....O...#....#...#O.....O.#.#O.O..O#......OO.O...#.#OO.#...O.O.O..#
        .#.O#.O.....O..OO...O..O..#....O#..O..O#....#......O#O....OO....#...O#O....#........O.O##..O....#...
        #.OOO#..##..O#.#....#.O##..#......O#..OO.....O.....O..OO..#..OO..O..#..#...O.....#.#..O.O.O..#.O...#
        #.O.#..#.....O.....#O.O...##.O....OO...OO.#....O.#.........O.O#.#....#.#......O....O..O....#.O....#O
        .#O...O.O....OO#.....O......#...O#..#.O#.O....#...O.O#..O...O...........#......#.##...OO......OO##..
        ........#.#O......#O..#OO....O......#.O.#O#O...O...#O....O...O.........O..OO..##...O.#.#OO#.....##.O
        .#.OOO.....#...#..O#....#.O....OO.O.O..OO..#.O..OOO.#....O.#..#O#O.#...O.#...O......#.O.O#O...O.OO..
        .#..#.O#...O....O....O...#.O..#.O...##.##O.O....O..#.#.#.O..#.O.OO..O...#..O#...##.O.....O...O....#.
        ...##...#.##OO.O.O...O...#...##.O..#OOO..#.OO#..O..O....O.O#.#.#O..##.O...O.O..O...O......#.......O.
        .##.#O..#....O........O..O.O..##...#...#O#...O.....O##.#..#.O........O........O##....#....#.O..O...O
        O.#.O..O..#..#O.##O.......O.O...O#.O......OO.O.O....O..#.O...#O.O..#..O....O..#..OO#.#.O#..#.#..#.#.
        ...................OO.#O..O...#.O...O...O.O#....#....O.OO.#O.O#.#.O#O.O#.#..O...OOOO..#..O...O.#..#.
        #.....#....#OO..O...O#..#.##....#.#..#.#O..#.O.O....#.#O.........##OOO...OO...O..#.##.O#..O.#....#..
        O..#.##....O##.....O.......O.#...#...#.##.....OO.O..O#.#O.#....#.....#.....#.....O.....#............
        #..#..#...O.#....#......O...#...#.#O.........#O#.#O...O...O...#.#.......#O...............O#....O....
        ##.#..OO..OO#...#.OO.....#....O#O...O.O.O.#....#......O...O#..OO.O..#.#...O.#O...O...#........O.O.O#
        O.#...O..#.#.O...#O..O#..O.#..O#O#OOO.......#..#O..#....O#...O.O...O....O.............OO..O..O#.#...
        O##.OO....#..#.....O..O..#..O.#...O..OO.......#...#.#....#...##.#.....#..#..OO#O.#..OO..O#..#..#...O
        #.O.#...#O.#...#.OO.OO..##.#...#.....O#.O#O.OO.........O...O..O.O...#.........O......OO..#..O...#O..
        .....#....O.##..O#..O.....#.O.....O...O.OO#OO.O......O..O..O.....#.#...#.O..#...O.O#.OOO.O.#....O...
        ..O...#....O....#.O.O#.#.#.O.OOO........O..OO..O##.....##.....#.O.......#....#.#O.O.#..#.O...#..#..O
        O#...O...##.#.#..O#O#......#.O..#....O...OO.#...#.OOO##..O.O#.#.#..O#OO.OO###.....O..#...#O.#..O....
        O.OO..#...O..O......O.#....O.O##....O.#O.O.O###..O...#..#.....#....O###..#...#O.OOO..O.#O.....#.....
        #O....#....O..O..O#.O.OOO...O.OOO......#....O.##O##O....#.OO..O#..#......O#.........#.#...OO...O....
        .#..OO.....O..#....O..........O..O.O..O.##...O.O.O.#.O.#...#O..#....O.#........#.#..O.##....#O##.#.#
        .OO.......O..O#.O..#OOO.O...#.#.O#.##....#.O..#.#.O.OO......#O##.O...........OO..#.......#...O#.....
        ....#......#..........#.#.O..O.....#...O....O.O.OO#.#......O..#.#O..OO..OO#.O#.#O#.O..O.O......#...#
        O.O.O..#O#......O.#O..#####...O.....#.O..#..O.........O...##.#O.....##.....#..#.....O.#...#O.#O#OO.O
        .....O..O#...O..#...O.......O..###O...O..O...OO.O...O..O#OO.....O#.O.#.O......#........O.O.O..OO#.O.
        .O...#.O....O#OO...OO#.#.......OO.....#.#.....#O..#..#.#.#O#..#.O.O.....##.#.#.#...#O...O......O....
        .#..#.OO....O.#..O..O..O...O..........O.#.OO..#..O............O#.O.#.O#...OO...O#.O.O.###.#O.#..O.O.
        ..#O...#..#..O....#............O..#.O....#...O...#.....O..##.##OO#....#...O#.O.O....OO#O..##..O...#O
        ..OO.#O#....O..#..#..O.#O..O....O.........#.O...#.O....##..#.O........O....O...#.OO..#........O.OOO.
        .O..#.OOO.O.O..O...#O..#..OO.....##....#..#..O.OO#O...#.O...#.....O#..##.##.#.....O..O....O..#O..OO.
        ...#.O.#.#.....O...#....O..O..##OO.........O.#..O..O......O#.#....O.O..O..O.......O.#.#..#...##...O.
        ..O....##...O...O.#OOOO.O..#.....OO.O.......#O..O..#..O...#....OO....O...##.#....##....O...O...O##.O
        O..O#.....#O...O...#O...#...O.....#......O...#..#O............#.###O.....O.....O.O.#..#OOOO...#O#...
        O.O...OO.##....#....#.#.#O....O.#.#..O..O..O.....OOO#.#.......#.....O...O...O...#..#....OO.#.O.....#
        ..#.#.O.O...O..#..O#..O..#..#.OO..##......#OO#....#.O.O.O##..O...O#..#O.........OO.#...OO.O.O.OOO...
        .......O.O..#.......O.O..#.O#..#...O.......O....O....##OOOO..#....#.#....#.....#O#....#.....O..OO.#.
        O..#OO..#.##.......##..O..O.#..O.O##.....OOO#..#....#..O.O..O....#..O.O.....#O..#.OO..O#....#.#.....
        OOO..O.....##....O..#.O.#...O##OOOOO....O.#..O.O#.O..##O.O#OO...O........O.O..O..O..#.O..OOO..#.O.OO
        ...O.O.O..OOO..O..#...#..O...##O#OO.OO..O.........O.....O#O.O.O....#..O#.O#..O.O.O.#.#O##O..#.......
        OO....O...OO..#..#OO..#......#.O.OO.O.O.#.......#OO........OO...#..O...##..O.....O...O.O#O.O.O#OO...
        O...O#.OO.....O.O.O...#O.O..O#O........#O.#....#...#.O.#...OOO#..........O.....O...##.....O#O.#.O##.
        ...O....#.O......OO......##..O..O.O....##........O.....#....##...##..#........#..##..O....O.O.#..O#O
        ..##.O....#.O##.OO#O....#OO#OO....O#.O......##..##.O..OO.O...O....O...OO....#.O..O....O#..#...#....O
        .###....#OOO...#....OOO.#..#....O.O#.......#............O......#...#..##..O#..O..O.##.O...O#....O...
        ..##O..#OO#...O....##.O..#...O.....#.O..O.O.....O..#O#O...##.#O.#....#OOO..O....O....#...OOO.#O..##.
        .O.O......#OO.......#.O.....#...OOO.O.O.#.O..#.O..##.O..O..O...O.#O##.O....#......#.O.#......#....O.
        ##......O.OO..O#.#O.###O....#...O#......##.......O.OO#O.....O....OO.........#....O.#.O.......O#...#.
        .O.....##..#....#.O.....O.#..OO...#O...#.#...##....O....#OO.#.O.#O.....#O.O.O#O.OO.....#...OO#...O.O
        .O#....OO.OO..O..OO.O....##...#..OO.O....O...O.O..O..O..O..#OO...#O...O...O.OO#...O.O.....#O....O...
        #O......O#....OO###.O...O##...#.........O.....O..##.##....O......O##....#...#..O...O.O.......O...###
        .....O##O..O..####.#O.OO..#..#..OO.#O.....O...O####.#......#..O....O.#.#......OOOOO.O.O...#.##......
        O##.#..#..#.#..#.#....#......OO#...O..O#..OO.#O.....O.........O#..#.......#.....##...#O#.#O..OO.....
        .O..O#O..#.OO.O....O..##O......O.##...O...#.O#.........O...O.O...O.#...OO.........#...#..#OO#.#....#
        ........O#....OO.#.O..O...OO#O..OO#OOO.O#.#.#O..#.....O.OO...O...OO.#..O..O....##..O#...OOO.O.##.O..
        ..#.O....##O.O.#.#....O.#.O.#...OO.O.....#..O.....O....##.......O#.......O.#..O.#.O#.O.O..##......O.
        #O#O.#...OOOO..OOO.O###....OO....#.O..OOO#..O...#....O.....O..OO.#.O..O###.O...O..#.#...OO...O......
        ......O#.O..#.O.......OOOO..#.O........O.#O##.#.#O#O.....O.#O....#...O...OO.O......OO........O.#..#.
        O..#..O..##..O.O....#....#..#O...OOO.OO.#O...#.........O..#..O........O#....O.#O#.#O.OO.......O.....
        ..O.OO#..O..O......O...OO...#.....#.....O......O.....O..#....#.....O.O..O#..O.#...#...#O..#..O..O...
        O.#..O.#O.OO.O#..OO...O#O..OO..O...#.O..#O..#...O....OO#..OO.....OOOO...#O...O#O..OO.........#......
        ....O.O#.#......O.O#....O#.......#....#.#.#O.#O...O#O.#..#.#.OO........O.#.#O....O#.......#..OO#O.O.
        ...O...O..###..#......#.#.O..O....OO##..##OO.......O...O#..OO#OO..#..O........O...#.#.#O.....#O#OOOO
        ...O..O.O#.O.#......O.#OO..OO.O....O.O....#.#O#.O.....O.....O..O.#.OO.....O...O.......O....O.#....O.
        #..O....O.O.O#..O..#..........#O...##..OO.#.O.O#O...#..O...#.......O.........O....O#O#O.O.O.#.OO.OO#
        O...#.....O..O#.#O...O...O.##..#O..#.##.O...O##.#O...O..O..O#....#.O..#O##..#...O.O.O..##..OO.O....O
        #.....#.O....O......OO...OO.#.O..O#..O.O#O......#O...#.#..O.#...#.O.#..#..#....O.O....OOO#..O.......
        #....#...O#.....O..O.#...O.O..O#..#.O.O.#...#.O..O#.......O......O..O....O....##OO.#O....##.OO....#.
        O...O.O..#..O#..#O.....#.#.O#O.O......#OOO...OO........O#.O.....#..#.#..#.O.#....#.......OO.#....#O.
        OO.##.#O...#.O.....O..#.#...#OO......##O......O..###...#.......O#.OO..O...#.#.....O.O......O##......
        #.O....OO.O.OO.....OO..O...........O..O..#OO#...O#....OO.O.......#.#.OO..OO.OO.#.O...O.#O.O........#
        ..##...O.O.O.O.O...OO.O...O..O.#.#......O.#.#.O.....#.O...O#..O.##O...#....O..#...O.OO.........O#.#.
        .....OOO#O#OO.O...#......#.O..##OOO#.#.#O.O.#O..#O..O..##O.#.#.....#.....#.#...OO.......O#...O....O#
        O..##.##...O...O.O#..#....O..O.....O#O#O#O#O....#.O.#O..#....O.O...O..O.#...O.OO..O..O.O#..#O##.#O.O
            """;
    
}
