"""
Runs commands from the Starlink CUPID package.

Autogenerated from the starlink .hlp and .ifl files,
by starlink-pywrapper/helperscripts/generate_functions.py.
"""

from . import wrapper


def clumpinfo(ndf, **kwargs):
    """
    Obtain information about one or more previously identified clumps.

    Runs the command: $CUPID_DIR/clumpinfo .

    Arguments
    ---------
    ndf : str,filename
        Input NDF containing clump identifications


    Keyword Arguments
    -----------------
    clumps : str
        The indices of the clumps to use [ALL]

    quiet : bool
        Supress screen output? [FALSE]


    Returns
    -------
    flbnd : List[float]

    fubnd : List[float]

    lbound : List[int]

    nclumps : int

    ubound : List[int]


    Notes
    -----
    See http://www.starlink.ac.uk/cgi-bin/htxserver/sun255.htx/sun255.html?xref_CLUMPINFO
    for full documentation of this command in the latest Starlink release

    """
    return wrapper.starcomm("$CUPID_DIR/clumpinfo", "clumpinfo", ndf, **kwargs)


def cupidhelp(*args, **kwargs):
    """
    Display information about CUPID.

    Runs the command: $CUPID_DIR/cupidhelp .

    Keyword Arguments
    -----------------
    topic : str
        Help topic [" "]

    subtopic : str
        Help subtopic [" "]

    subsubtopic : str
        Help subsubtopic [" "]

    subsubsubtopic : str
        Help subsubsubtopic [" "]


    Notes
    -----
    See http://www.starlink.ac.uk/cgi-bin/htxserver/sun255.htx/sun255.html?xref_CUPIDHELP
    for full documentation of this command in the latest Starlink release

    """
    return wrapper.starcomm("$CUPID_DIR/cupidhelp", "cupidhelp", *args, **kwargs)


def extractclumps(mask, data, out, outcat, **kwargs):
    """
    Extract previously identified clumps of emission from an NDF.

    Runs the command: $CUPID_DIR/extractclumps .

    Arguments
    ---------
    mask : str,filename
        Input mask NDF

    data : str,filename
        Input data NDF

    out : str,filename
        Output mask NDF

    outcat : str
        Output catalogue


    Keyword Arguments
    -----------------
    backoff : bool
        Remove background when finding clump sizes? [TRUE]

    deconv : bool
        Correct clump parameters for beam smoothing? [TRUE]

    fwhmbeam : float
        Spatial beam width in pixels [dyn.]

    jsacat : str
        Output JSA-style catalogue [!]

    logfile : str
        Name of output log file [!]

    shape : str
        Spatial clump shape in output catalogue [dyn.]

    velores : float
        Velocity resolution in channels [dyn.]

    wcspar : bool
        Use WCS units in the output catalogue? [dyn.]


    Returns
    -------
    nclumps : int


    Notes
    -----
    See http://www.starlink.ac.uk/cgi-bin/htxserver/sun255.htx/sun255.html?xref_EXTRACTCLUMPS
    for full documentation of this command in the latest Starlink release

    """
    return wrapper.starcomm("$CUPID_DIR/extractclumps", "extractclumps", mask, data, out, outcat, **kwargs)


def findback(in_, out, **kwargs):
    """
    Estimate the background in an NDF by removing small scale structure.

    Runs the command: $CUPID_DIR/findback .

    Arguments
    ---------
    `in_` : str,filename
        Input NDF

    out : str,filename
        Output NDF


    Keyword Arguments
    -----------------
    box : List[int]
        Filter dimensions, in pixels [9]

    msg_filter : str
        Information level [NORM]

    newalg : bool
        Use experimental algorithm variations? [FALSE]

    rms : float
        RMS noise level

    sub : bool
        Subtract background from input data? [FALSE]

    wlim : float
        Weight limit for good output pixels [0.3]


    Notes
    -----
    See http://www.starlink.ac.uk/cgi-bin/htxserver/sun255.htx/sun255.html?xref_FINDBACK
    for full documentation of this command in the latest Starlink release

    """
    return wrapper.starcomm("$CUPID_DIR/findback", "findback", in_, out, **kwargs)


def findclumps(in_, out, **kwargs):
    """
    Identify clumps of emission within a 1, 2 or 3 dimensional NDF.

    Runs the command: $CUPID_DIR/findclumps .

    Arguments
    ---------
    `in_` : str,filename
        Input NDF

    out : str,filename
        Output NDF


    Keyword Arguments
    -----------------
    outcat : str
        Output KAPPA-style catalogue [!]

    method : str
        Clump identification algorithm [current value]

    backoff : bool
        Remove background when finding clump sizes? [dyn.]

    config : str
        Algorithm tuning parameters [current value]

    deconv : bool
        Correct clump parameters for beam smoothing? [TRUE]

    jsacat : str
        Output JSA-style catalogue [!]

    logfile : str
        Name of output log file [!]

    msg_filter : str
        Information level [NORM]

    perspectrum : bool
        Process spectra independently of neighbouring spectra? [FALSE]

    qout : str,filename
        Copy of input NDF with Quality mask [!]

    repconf : bool
        Report supplied configuration? [current value]

    rms : float
        RMS noise level

    shape : str
        Spatial clump shape in output catalogue [dyn.]

    wcspar : bool
        Use WCS units in the output catalogue? [dyn.]


    Returns
    -------
    nclumps : int


    Notes
    -----
    See http://www.starlink.ac.uk/cgi-bin/htxserver/sun255.htx/sun255.html?xref_FINDCLUMPS
    for full documentation of this command in the latest Starlink release

    """
    return wrapper.starcomm("$CUPID_DIR/findclumps", "findclumps", in_, out, **kwargs)


def makeclumps(out, outcat, **kwargs):
    """
    Create simulated data containing clumps and noise.

    Runs the command: $CUPID_DIR/makeclumps .

    Arguments
    ---------
    out : str,filename
        Output NDF

    outcat : str
        Output catalogue


    Keyword Arguments
    -----------------
    angle : List[float]
        Mean and width of spatial position angles in degs [current value]

    beamfwhm : float
        Spatial FWHM of instrument beam in pixels [current value]

    deconv : bool
        Correct clump parameters for beam smoothing? [TRUE]

    fwhm1 : List[float]
        Mean and width of FWHMs on pixel axis 1 in pixels [current value]

    fwhm2 : List[float]
        Mean and width of FWHMs on pixel axis 2 in pixels [current value]

    fwhm3 : List[float]
        Mean and width of FWHMs on pixel axis 3 in pixels [current value]

    grid : int
        Margin to place round outside of regular grid [!]

    lbnd : List[int]
        Lower pixel bounds of output array [1,1]

    like : str,filename
        An NDF to define the output WCS [!]

    model : str,filename
        Output NDF without noise

    nclump : List[int]
        Number of clumps to create [50]

    pardist : str
        Parameter distribution [current value]

    peak : List[float]
        Mean and width of clump peak values [current value]

    precat : bool
        Create catalogue before instrumental smoothing is applied? [FALSE]

    rms : float
        RMS noise to add to data [current value]

    shape : str
        Spatial clump shape in output catalogue ["None"]

    trunc : float
        Truncation level for clumps [current value]

    ubnd : List[int]
        Upper pixel bounds of output array [200,200]

    velfwhm : float
        FWHM of velocity resolution in pixels [current value]

    vgrad1 : List[float]
        Mean and width of vel. gradient on axis 1 [current value]

    vgrad2 : List[float]
        Mean and width of vel. gradient on axis 2 [current value]


    Notes
    -----
    See http://www.starlink.ac.uk/cgi-bin/htxserver/sun255.htx/sun255.html?xref_MAKECLUMPS
    for full documentation of this command in the latest Starlink release

    """
    return wrapper.starcomm("$CUPID_DIR/makeclumps", "makeclumps", out, outcat, **kwargs)


def outlineclump(*args, **kwargs):
    """
    Draw an outline around a 2-dimensional clump identified by CUPID.

    Runs the command: $CUPID_DIR/outlineclump.csh .

    Keyword Arguments
    -----------------
    index : 
           The integer index or indices of the clumps to be identified.
       For multiple indices supply a comma-separated list, using
       hyphens to express ranges.  For example "2,4-6,9" would draw
       the outlines of clumps with indices 2, 4, 5, 6, and 9.

    ndf : 
           The name of the NDF containing the clump information. This NDF
       should have been created using the CUPID:FINDCLUMPS or
       CUPID:EXTRACTCLUMPS command. The clump cut-out images contained in
       the CUPID extension of this NDF will be used to define the outline
       of the clump.

    style : 
           A group of attribute settings describing the plotting style to
       use for the outline.

       A comma-separated list of strings should be given in which each
       string is either an attribute setting, or the name of a text
       file preceded by an up-arrow character "^".  Such text files
       should contain further comma-separated lists which will be read
       and interpreted in the same manner.  Attribute settings are
       applied in the order in which they occur within the list, with
       later settings overriding any earlier settings given for the
       same attribute.

       Each individual attribute setting should be of the form:

          <name>=<value>

       where <name> is the name of a plotting attribute, and <value>
       is the value to assign to the attribute. Default values will be
       used for any unspecified attributes.  All attributes will be
       defaulted if a null value (!) is supplied.  See section
       "Plotting Attributes" in SUN/95 for a description of the
       available attributes.  Any unrecognised attributes are ignored
       (no error is reported).

       The appearance of the clump outline is controlled by the attributes
       Colour(Curves), Width(Curves), etc (the synonym Contours may be
       used in place of Curves). The contour appearance established in
       this way may be modified using parameters PENS, PENROT and
       DASHED. [current value]


    Notes
    -----
    See http://www.starlink.ac.uk/cgi-bin/htxserver/sun255.htx/sun255.html?xref_OUTLINECLUMP
    for full documentation of this command in the latest Starlink release

    """
    return wrapper.starcomm("$CUPID_DIR/outlineclump.csh", "outlineclump", *args, **kwargs)

