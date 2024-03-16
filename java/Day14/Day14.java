import java.util.ArrayList;


public class Day14
{
    private static ArrayList< ArrayList< Character > > rocks;

    /**
     * @param input     the rock map as multiline String
     * @param justNorth for part1 set to true
     * @param cycles    for part1 set to 1; part2 1000000000
     * @return
     */
    public static int run( String input, boolean justNorth, int cycles )
    {
        // parse the INPUT and populate rocks
        parseLines( input );
        String prevIteration = "";

        for( int i=0; i<cycles; i++ )
        {
            System.err.println("Running " + i + "/" + cycles + " " + i*100/cycles + "%" );
            String startOfIteration = printRocks( );
            if( prevIteration == startOfIteration )
            {
                break;
            }          
            prevIteration = startOfIteration;

            rollNorth( );
            if( ! justNorth )
            {
                rollWest( );
                rollSouth( );
                rollEast( );
            }   
        }   
        int weight = calculateTotalWeight( );
        return weight;
    }

    public static void main( String[] args )
    {
        run( TestData.FULL_MAP, true, 1 );
    }

    /**
     * @param input the rocks playfield
     * returns nothing. just populates Day14_1.rocks
     */
    public static void parseLines( String input )
    {
        rocks = new ArrayList< ArrayList< Character > >( );

        String[] lines = input.split("\\n");

        for( String line : lines )
        {
            ArrayList< Character > row = new ArrayList< Character >();
            
            for( int i=0; i<line.length(); i++ )
            {
                row.add( line.charAt(i) );
            }
            rocks.add( row );
        }

        printRocks();
    }

    public static String printRocks( )
    {
        ArrayList<String> retval = new ArrayList<String>( );

        for( ArrayList< Character > row : rocks )
        {
            String rowStr = "";
            for( Character c : row )
            {
                rowStr = rowStr + c;
            }
            retval.add( rowStr );
        }
        return String.join("\n",retval);
    }

    public static void rollNorth( )
    {
        for( int row = 1; row < rocks.size(); row++ )  // Skip row #0 - it cant be rolled.
        {
            ArrayList<Character> rockRow = rocks.get(row);
            for( int col = 0; col < rockRow.size(); col++ )
            {
                Character c = rockRow.get(col);
                if( c == Character.valueOf('O') )
                {
                    rollRockNorth( row, col );
                }
            }
        }        
    }

    public static void rollRockNorth( int row, int col )
    {
        rocks.get(row).set( col, '.' );

        // Start iterating up through the rows until we feed a rock: 'O' or '#'
        // or hit row 0
        for( int r=row-1; r>=0; r-- )
        {
            char positionAbove = rocks.get(r).get(col);
            if( positionAbove == 'O' || positionAbove == '#' )
            {
                rocks.get(r+1).set( col, 'O' );
                break;
            }
            else if( r == 0 )
            {
                rocks.get(0).set( col, 'O' );
                break;
            }
        }
    }

    //////////////////////////////////////////////////////////

    public static void rollSouth( )
    {
        for( int row = rocks.size()-2; row >= 0; row-- )  // Skip last row - it cant be rolled.
        {
            ArrayList<Character> rockRow = rocks.get(row);
            for( int col = 0; col < rockRow.size(); col++ )
            {
                Character c = rockRow.get(col);
                if( c == Character.valueOf('O') )
                {
                    rollRockSouth( row, col );
                }
            }
        }        
    }

    public static void rollRockSouth( int row, int col )
    {
        rocks.get(row).set( col, '.' );

        // Start iterating down through the rows until we feed a rock: 'O' or '#'
        // or hit the last row
        for( int r=row+1; r<rocks.size(); r++ )
        {
            char positionBelow = rocks.get(r).get(col);
            if( positionBelow == 'O' || positionBelow == '#' )
            {
                rocks.get(r-1).set( col, 'O' );
                break;
            }
            else if( r == rocks.size()-1 )
            {
                rocks.get( rocks.size()-1 ).set( col, 'O' );
                break;
            }
        }
    }

    /////////////////////////////////////////////////////////////

   public static void rollEast( ) // -> E
   {
        for( int row = 0; row < rocks.size(); row++ )
        {
            ArrayList<Character> rockRow = rocks.get(row);
            for( int col = rockRow.size()-2; col >= 0; col-- )
            {
                Character c = rockRow.get(col);
                if( c == Character.valueOf('O') )
                {
                    rollRockEast( row, col );
                }
            }
        }        
   }

   public static void rollRockEast( int row, int col )
   {
       rocks.get(row).set( col, '.' );

       // Start iterating across this rows until we find a rock: 'O' or '#'
       // or hit the last col.
       for( int c=col+1; c < rocks.get(row).size(); c++ )
       {
           char nextPos = rocks.get(row).get(c);
           if( nextPos == 'O' || nextPos == '#' )
           {
               rocks.get(row).set( c-1, 'O' );
               break;
           }
           else if( c == rocks.get(row).size()-1 )
           {
               rocks.get( row ).set( rocks.get(row).size()-1, 'O' );
               break;
           }
       }
   }
   
   ////////////////////////////////////////////////////////////

   public static void rollWest( ) // W <-
   {
        for( int row = 0; row < rocks.size(); row++ )
        {
            ArrayList<Character> rockRow = rocks.get(row);
            for( int col = 1; col < rockRow.size(); col++ ) // skip col 0
            {
                Character c = rockRow.get(col);
                if( c == Character.valueOf('O') )
                {
                    rollRockWest( row, col );
                }
            }
        }        
   }

   public static void rollRockWest( int row, int col ) // W <-
   {
       rocks.get(row).set( col, '.' );

       // Start iterating across this rows until we find a rock: 'O' or '#'
       // or hit the first col.
       for( int c=col-1; c >= 0; c-- )
       {
           char nextPos = rocks.get(row).get(c);
           if( nextPos == 'O' || nextPos == '#' )
           {
               rocks.get(row).set( c+1, 'O' );
               break;
           }
           else if( c == 0 )
           {
               rocks.get( row ).set( 0, 'O' );
               break;
           }
       }
   }
   
   ////////////////////////////////////////////////////////////

    public static int calculateTotalWeight( )
    {
        int total   = 0;
        int numRows = rocks.size();
        for( int row = 0; row < rocks.size(); row++ ) 
        {
            ArrayList<Character> rockRow = rocks.get(row);
            for( int col = 0; col < rockRow.size(); col++ )
            {
                Character c = rockRow.get(col);
                if( c == Character.valueOf('O') )
                {
                    total = total + (numRows - row);
                }
            }
        }   
        System.out.println( "calculateTotalWeight: " + total );
        return total;
    }
}

