def get_file_extension(data: bytes) -> str:
    """
    Determine the file extension based on the magic numbers in the byte buffer.
    Returns 'unknown' if the signature isn’t recognized.
    """
    if not data or len(data) < 4:
        return 'unknown'

    # First 4 bytes as lowercase hex
    header = data[:4].hex().lower()

    if header in ('ffd8ffe0', 'ffd8ffe1', 'ffd8ffe2', 'ffd8ffe3', 'ffd8ffe8'):
        return 'jpg'

    if header == '89504e47':
        return 'png'

    if header == '47494638':
        return 'gif'

    if header == '25504446':
        return 'pdf'

    if header == '74657874':
        return 'txt'

    if header == '52494646':
        # RIFF container – check bytes 8–12
        riff_type = data[8:12].hex().lower()
        if riff_type == '57415645':
            return 'wav'
        if riff_type == '41564920':
            return 'avi'
        return 'webp'

    if header in ('504b0304', '504b0506', '504b0708'):
        # ZIP-based files: read up to N bytes as utf-8 to spot Office content
        sample = data[:5000].decode('utf-8', errors='ignore').lower()
        if '[content_types].xml' in sample:
            if 'xl/workbook.xml' in sample:
                return 'xlsx'
            if 'word/document.xml' in sample:
                return 'docx'
            if 'ppt/presentation.xml' in sample or 'ppt/' in sample:
                return 'pptx'
        return 'zip'

    if header == 'd0cf11e0':
        # Older Microsoft CFBF files; check sector at offset 512
        sub = data[512:516].hex().lower()
        if sub == 'eca5c100':
            return 'doc'
        if sub == 'e11ab1a1':
            return 'xls'
        return 'cfb'

    if header == '52617221':
        return 'rar'

    if header == '3c3f786d':
        return 'xml'

    if header == '3c737667':
        return 'svg'

    if header == '49443303':
        return 'mp3'

    if header in ('000001ba', '000001b3'):
        return 'mpg'

    if header == '4d546864':
        return 'midi'

    if header == '1f8b0800':
        return 'gz'

    return 'unknown'
