import org.junit.Test;
import static org.junit.Assert.assertEquals;

//import java.util.ArrayList;

public class Day14Test {

    @Test
    public void testRunPart1() {
        // Part1 tests
        assertEquals( Day14.run( TestData.SMALL_MAP, true, 1 ), 136 );
        assertEquals( Day14.run( TestData.FULL_MAP,  true, 1 ), 106517 );
    }

    @Test
    public void testRunPart2() {
        // Part2 test
        //assertEquals( Day14.run( TestData.SMALL_MAP, true, 1000000000 ), 64 );
    }

    @Test
    public void testRollNorth() {
        String INPUT = """
        O.......
        .O.##...
        .O......
        ...OO...        
        """;

        String EXPECTED = """
        OO......
        .O.##...
        ...OO...
        ........        
        """;
        Day14.parseLines( EXPECTED );
        String expected = Day14.printRocks( );

        Day14.parseLines( INPUT );
        Day14.rollNorth( );
        String actual = Day14.printRocks( );
        
        assertEquals( expected, actual );
    }

    @Test
    public void testRollSouth() {
        String INPUT = """
        O.......
        .O.OO...
        .O..#...
        .#.#....        
        """;

        String EXPECTED = """
        ........
        .O..O...
        .O.O#...
        O#.#....      
        """;
        Day14.parseLines( EXPECTED );
        String expected = Day14.printRocks( );

        Day14.parseLines( INPUT );
        Day14.rollSouth( );
        String actual = Day14.printRocks( );
        
        assertEquals( expected, actual );
    }    

    @Test
    public void testRollEast() {
        String INPUT = """
        O...
        .O#.
        .OO.
        .O.#        
        """;

        String EXPECTED = """
        ...O
        .O#.
        ..OO
        ..O#             
        """;
        Day14.parseLines( EXPECTED );
        String expected = Day14.printRocks( );

        Day14.parseLines( INPUT );
        Day14.rollEast( );
        String actual = Day14.printRocks( );
        
        assertEquals( expected, actual );
    }    


    @Test
    public void testRollWest() {
        String INPUT = """
        O....
        #O...
        #...O
        ...OO
        .#.OO        
        """;

        String EXPECTED = """
        O....
        #O...
        #O...
        OO...
        .#OO.
        """;
        Day14.parseLines( EXPECTED );
        String expected = Day14.printRocks( );

        Day14.parseLines( INPUT );
        Day14.rollWest( );
        String actual = Day14.printRocks( );
        
        assertEquals( expected, actual );
    }    


    @Test
    public void testOneCycle() {
        String EXPECTED1 = """
        .....#....
        ....#...O#
        ...OO##...
        .OO#......
        .....OOO#.
        .O#...O#.#
        ....O#....
        ......OOOO
        #...O###..
        #..OO#....
        """;
        Day14.parseLines( EXPECTED1 );
        String expected = Day14.printRocks( );

        Day14.run( TestData.SMALL_MAP, false, 1 );
        String actual = Day14.printRocks( );
        
        assertEquals( expected, actual );
    }

    @Test
    public void testThreeCycles() {

        // after 3 cycles.
        String EXPECTED3 = """
        .....#....
        ....#...O#
        .....##...
        ..O#......
        .....OOO#.
        .O#...O#.#
        ....O#...O
        .......OOO
        #...O###.O
        #.OOO#...O
        """;        
        Day14.parseLines( EXPECTED3 );
        String expected = Day14.printRocks( );        

        Day14.run( TestData.SMALL_MAP, false, 3 ); // 3 cycles
        String actual = Day14.printRocks( );

        assertEquals( expected, actual );
    }    

}
