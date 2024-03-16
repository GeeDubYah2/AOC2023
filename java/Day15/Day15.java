//import java.util.ArrayList;

    // Part2 notes
    // 
    // Each init sequence consists of:
    //  . letters are a label -> hash of these letters returns the box number 
    //  . symbol - one of = or -
    //    . "=" - is followed by the focal length (1 to 9) that needs to go into the box. Keep the label
    //      . if lens with matching label - replace the old lens with the new.
    //      . if no lens with matching label - and lens behind any other lens.
    //    . "-" - go to the relevent box (using hash) and the lens with the matching label (letter string)
    //      . shuffle all other lenses forward.

    // e.g. 
    //   "rn=1" - hash("rn")=1
    //     - lensFL = 1
    //     - box[1] add lens 1
    //   "cm-" - hash("cm")=1
    //     - remove the lens "cm" from box[0] if its there.

    // box[0] : [ "rm 1", "cm 2", "ab 5" ]
    // ArrayList< LinkedHashMap< String, Integer > > boxes
    // 
    // LinkedHashMap can be used to lookup by key, but can also iterate in insertion order.

import java.util.ArrayList;
import java.util.LinkedHashMap;

public class Day15
{
    private static ArrayList< LinkedHashMap< String, Integer > > boxes;

    public static void main( String[] args )
    {
        int hash = calculateHashFullSequence( TestData.FULL_TEST );
        System.out.println( "PART1: " + hash );
    }

    public static int calculateHash( String str )
    {
        int hash = 0;

        for( int i=0; i<str.length(); i ++)
        {
            hash += (int)str.charAt(i);
            hash *= 17;
            hash = hash % 256;
        }
        return hash;
    }

    public static String[] tokenise( String str )
    {
        str = str.replace("\n", "");
        return str.split(",");
    }

    // part 1 - calculate the hash for the full sequence.
    public static int calculateHashFullSequence( String str )
    {
        int total = 0;
        String[] words = tokenise(str);
        for( String word : words )
        {
            total += calculateHash(word);
        }
        return total;
    }

    protected static void initBoxes( )
    {
        boxes = new ArrayList< LinkedHashMap< String, Integer > >( );
        for( int i=0; i<256; i++ )
        {
            boxes.add( new LinkedHashMap< String, Integer >( ) );
        }
    }

    // part 2 - put lenses in boxes, then calculate focussing power.
    public static void putLensesInBoxes( String str )
    {
        initBoxes( );

        // rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7
        // split sequence into the comma separated words
        String[] words = tokenise(str);

        for( String word : words )
        {
            if( word.indexOf('=')>0 )
            {
                addToBox( word );
            }
            else if( word.indexOf('-')>0 )
            {
                removeFromBox( word );
            }
        }
    }

    public static int calculateFocalPower( )
    {
        int total = 0;
        for( int boxIdx=0; boxIdx<boxes.size(); boxIdx++ )
        {
            LinkedHashMap< String, Integer > box = boxes.get(boxIdx);
            int slot = 0;
            for( String label : box.keySet() )
            {
                slot++;
                total += (boxIdx+1) * slot * box.get(label);
            }
        }
        return total;
    }

    public static void addToBox(String word) 
    {
        String[] tokens = word.split("=");
        String label    = tokens[0];
        int hash = calculateHash(label);
        int fl   = Integer.valueOf(tokens[1]);

        LinkedHashMap< String, Integer > box = boxes.get(hash);
        box.put( label, fl );
    }

    public static void removeFromBox(String word) 
    {
        String[] tokens = word.split("-");
        String label    = tokens[0];
        int hash = calculateHash(label);

        LinkedHashMap< String, Integer > box = boxes.get(hash);
        box.remove( label );    
    }

    public static String printBoxes( )
    {
        String retval = "";
        for( int i=0; i<boxes.size(); i++ )
        {
            LinkedHashMap< String, Integer > box = boxes.get(i);
            if( box.size() > 0 )
            {
                retval = retval + "\nBox[" + i + "] : ";

                for( String label : box.keySet() )
                {
                    retval = retval + "[" + label + " " + box.get(label) + "] ";
                }
            }   
        }

        return retval;
    }

}