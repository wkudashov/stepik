with open('5.1.3.html', 'w') as ouf:
    ouf.write("<html><body><table>")
    for i in range(1, 11):
        ouf.write('<tr>')
        for j in range(1, 11):
            ouf.write(f'<td><a href=http://{i*j}.ru>{i*j}</a></td>')
        ouf.write('</tr>')
    ouf.write("</table></body></html>")
