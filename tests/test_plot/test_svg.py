"""
Tests of SVG format.

For debug information use:
pytest-3 --log-cli-level debug
"""
from . import context
PS_DIR = 'SVG'


def test_svg(test_dir):
    prj = 'simple_2layer'
    ctx = context.TestContext(test_dir, prj, 'svg', PS_DIR)
    ctx.run()
    ctx.expect_out_file(ctx.get_gerber_filename('F_Cu', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('F_Fab', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_job_filename())
    ctx.clean_up()


def test_svg_all(test_dir):
    prj = 'simple_2layer'
    ctx = context.TestContext(test_dir, prj, 'svg_all', PS_DIR)
    ctx.run()
    ctx.expect_out_file(ctx.get_gerber_filename('B_'+context.DEF_ADHES, '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('B_'+context.DEF_CRTYD, '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('B_Cu', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('B_Fab', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('B_Mask', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('B_Paste', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('B_'+context.DEF_SILKS, '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename(context.DEF_CMTSU, '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename(context.DEF_DWGSU, '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename(context.DEF_ECO1U, '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename(context.DEF_ECO2U, '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('Edge_Cuts', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('F_'+context.DEF_ADHES, '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('F_'+context.DEF_CRTYD, '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('F_Cu', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('F_Fab', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('F_Mask', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('F_Paste', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('F_'+context.DEF_SILKS, '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('Margin', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_job_filename())
    ctx.clean_up()


def test_svg_selected(test_dir):
    prj = 'simple_2layer'
    ctx = context.TestContext(test_dir, prj, 'svg_selected', PS_DIR)
    ctx.run()
    ctx.dont_expect_out_file(ctx.get_gerber_filename('B_'+context.DEF_ADHES, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('B_'+context.DEF_CRTYD, '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('B_Cu', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('B_Fab', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('B_Mask', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('B_Paste', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('B_'+context.DEF_SILKS, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename(context.DEF_CMTSU, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename(context.DEF_DWGSU, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename(context.DEF_ECO1U, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename(context.DEF_ECO2U, '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('Edge_Cuts', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('F_'+context.DEF_ADHES, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('F_'+context.DEF_CRTYD, '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('F_Cu', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('F_Fab', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('F_Mask', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('F_Paste', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('F_'+context.DEF_SILKS, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('Margin', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_job_filename())
    ctx.clean_up()


def test_svg_copper_and_user(test_dir):
    prj = 'good-project'
    ctx = context.TestContext(test_dir, prj, 'svg_copper_and_user', PS_DIR)
    ctx.run()
    ctx.expect_out_file(ctx.get_gerber_filename('B_Cu', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename(context.DEF_CMTSU, '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename(context.DEF_DWGSU, '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename(context.DEF_ECO1U, '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename(context.DEF_ECO2U, '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('Edge_Cuts', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('F_Cu', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('GND_Cu', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('Margin', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('Power_Cu', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('Signal1_Cu', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('Signal2_Cu', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('B_'+context.DEF_ADHES, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('B_'+context.DEF_CRTYD, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('B_Fab', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('B_Mask', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('B_Paste', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('B_'+context.DEF_SILKS, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('F_'+context.DEF_ADHES, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('F_'+context.DEF_CRTYD, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('F_Fab', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('F_Mask', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('F_Paste', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('F_'+context.DEF_SILKS, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_job_filename())
    ctx.clean_up()


def test_svg_copper_and_draw(test_dir):
    prj = 'good-project'
    ctx = context.TestContext(test_dir, prj, 'svg_copper_and_draw', PS_DIR)
    ctx.run()
    ctx.expect_out_file(ctx.get_gerber_filename('B_Cu', '.svg'))
    # This name is selected manually:
    ctx.expect_out_file(ctx.get_gerber_filename('Dwgs_User', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('F_Cu', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('GND_Cu', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('Power_Cu', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('Signal1_Cu', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('Signal2_Cu', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('Margin', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename(context.DEF_ECO1U, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename(context.DEF_ECO2U, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('Edge_Cuts', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename(context.DEF_CMTSU, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('B_'+context.DEF_ADHES, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('B_'+context.DEF_CRTYD, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('B_Fab', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('B_Mask', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('B_Paste', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('B_'+context.DEF_SILKS, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('F_'+context.DEF_ADHES, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('F_'+context.DEF_CRTYD, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('F_Fab', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('F_Mask', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('F_Paste', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('F_'+context.DEF_SILKS, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_job_filename())
    ctx.clean_up()


def test_svg_copper_and_cmt(test_dir):
    prj = 'good-project'
    ctx = context.TestContext(test_dir, prj, 'svg_copper_and_cmt', PS_DIR)
    ctx.run()
    ctx.expect_out_file(ctx.get_gerber_filename('B_Cu', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('F_Cu', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('GND_Cu', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('Power_Cu', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('Signal1_Cu', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('Signal2_Cu', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename(context.DEF_CMTSU, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename(context.DEF_DWGSU, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('Margin', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename(context.DEF_ECO1U, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename(context.DEF_ECO2U, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('Edge_Cuts', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('B_'+context.DEF_ADHES, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('B_'+context.DEF_CRTYD, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('B_Fab', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('B_Mask', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('B_Paste', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('B_'+context.DEF_SILKS, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('F_'+context.DEF_ADHES, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('F_'+context.DEF_CRTYD, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('F_Fab', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('F_Mask', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('F_Paste', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('F_'+context.DEF_SILKS, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_job_filename())
    ctx.clean_up()


def test_svg_anchor(test_dir):
    prj = 'good-project'
    ctx = context.TestContext(test_dir, prj, 'svg_anchor', PS_DIR)
    ctx.run(extra=['SVG'])
    assert ctx.search_out(r"- 'SVG files' \(SVG\) \[svg\]")
    ctx.expect_out_file(ctx.get_gerber_filename('B_Cu', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('F_Cu', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('GND_Cu', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('Power_Cu', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('Signal1_Cu', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('Signal2_Cu', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename(context.DEF_CMTSU, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename(context.DEF_DWGSU, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('Margin', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename(context.DEF_ECO1U, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename(context.DEF_ECO2U, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('Edge_Cuts', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('B_'+context.DEF_ADHES, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('B_'+context.DEF_CRTYD, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('B_Fab', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('B_Mask', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('B_Paste', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('B_'+context.DEF_SILKS, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('F_'+context.DEF_ADHES, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('F_'+context.DEF_CRTYD, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('F_Fab', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('F_Mask', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('F_Paste', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('F_'+context.DEF_SILKS, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_job_filename())
    ctx.clean_up()


def test_svg_technical(test_dir):
    prj = 'good-project'
    ctx = context.TestContext(test_dir, prj, 'svg_technical', PS_DIR)
    ctx.run()
    ctx.dont_expect_out_file(ctx.get_gerber_filename('B_Cu', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('F_Cu', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('GND_Cu', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('Power_Cu', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('Signal1_Cu', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('Signal2_Cu', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename(context.DEF_CMTSU, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename(context.DEF_DWGSU, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('Margin', '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename(context.DEF_ECO1U, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename(context.DEF_ECO2U, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_filename('Edge_Cuts', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('B_'+context.DEF_ADHES, '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('B_'+context.DEF_CRTYD, '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('B_Fab', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('B_Mask', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('B_Paste', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('B_'+context.DEF_SILKS, '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('F_'+context.DEF_ADHES, '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('F_'+context.DEF_CRTYD, '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('F_Fab', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('F_Mask', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('F_Paste', '.svg'))
    ctx.expect_out_file(ctx.get_gerber_filename('F_'+context.DEF_SILKS, '.svg'))
    ctx.dont_expect_out_file(ctx.get_gerber_job_filename())
    ctx.clean_up()
