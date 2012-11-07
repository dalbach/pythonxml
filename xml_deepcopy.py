#!/usr/bin/env python

"""
xml_deepcopy.py

A minidom based xml copy utility.

The function xml_deepcopy() copies all nodes and attributes
from source_node to target_node in target_doc.

The function add_xmlstr2doc() is an example of using xml_deepcopy().

Run xml_deepcopy.py to run add_xmlstr2doc()
"""

from xml.parsers.expat import ExpatError
from xml.dom.minidom import parseString

#=============================================


def xml_deepcopy(target_doc, target_node, source_node):

    """
    xml_deepcopy()

      Recursively add source_node and all children to 
      target doc at target node.

      Returns new target_doc.
      Caller needs to catch ExpatError.
    """


    # Copy any attributes for the source node to the target node.
    if source_node.hasAttributes():
        attrs = source_node.attributes
        for key in attrs.keys():
            target_node.setAttribute(attrs[key].name, attrs[key].value)


    source_children = source_node.childNodes
    for source_child in source_children:

        source_child_nodetype = source_child.nodeType

        # Could be TEXT/CDATA or could be an ELEMENT.
        if source_child_nodetype == source_child.TEXT_NODE:
            # TEXT
            nodevalue = source_child.nodeValue
            node_text = target_doc.createTextNode(nodevalue)
            target_node.appendChild(node_text)

        elif source_child_nodetype == source_child.CDATA_SECTION_NODE:
            # CDATA
            nodevalue = source_child.nodeValue
            node_text = target_doc.createCDATASection(nodevalue)
            target_node.appendChild(node_text)

        else:
            # ELEMENT
            source_child_nodename = source_child.nodeName

            element_node = target_doc.createElement(source_child_nodename)
            new_target_node = target_node.appendChild(element_node)

            # Recursively process any children.
            if source_child.hasChildNodes():
                target_doc = xml_deepcopy(target_doc,
                                          new_target_node,
                                          source_child)

    return target_doc


#=============================================


def add_xmlstr2doc(source_xml_str, target_doc):

    """
    add_xmlstr2doc()

      Add a xml fragment into a target xml document.

      Returns new target_doc.
      Caller needs to catch ExpatError.
    """


    # Build the source document from the xml string.
    source_doc = parseString(source_xml_str)
    # Get the source document root node
    source_node = source_doc.firstChild
    source_nodename = source_node.nodeName

    # Add source document root node to the target document.
    element_node = target_doc.createElement(source_nodename)
    target_node = target_doc.lastChild.appendChild(element_node)

    # Recursively process the source nodes by adding to target document.
    target_doc = xml_deepcopy(target_doc,
                              target_node,
                              source_node)


    return target_doc


#=============================================


if __name__ == "__main__":

    target_xml = """
    <target_xml><message_list><message_type>email</message_type><pager_id>EMAIL0</pager_id><text_message>BOOKED EMAIL DISPATCHED</text_message><message_address>someone@somewhere.com</message_address><report_id>0000</report_id><message_type>email</message_type><pager_id>EMAIL1</pager_id><text_message>BOOKED EMAIL DISPATCHED</text_message><message_address>someone@somewhere.com</message_address><report_id>0001</report_id></message_list></target_xml>
            """

    source_xml = """
    <source_xml><transaction_id>suwillia1348459343995</transaction_id><agent_id>suwillia</agent_id><phone_id>6262</phone_id><host_addr>172.16.96.86</host_addr><process_id>1348450908145</process_id><client_id>1234640021</client_id><line_id>0000083842</line_id><pager_id>0001421900</pager_id><op_group>AM</op_group><recording_port><![CDATA[1942:027]]></recording_port><call_id>019383</call_id><call_offer_time>20120924000100</call_offer_time><call_origination>answer</call_origination><call_start_time>20120924000106</call_start_time><call_end_time>20120924000223</call_end_time><elapsed_time>78</elapsed_time><custom_form_message><form_id>29464636</form_id><form_class>custom</form_class><format_for_csv>false</format_for_csv><csv_prefix><![CDATA[]]></csv_prefix><element_list><element name="TI1311864813976" sequence_nr="10" include_when_blank="false"><value><input><![CDATA[]]></input></value><separator><![CDATA[CRLF]]></separator></element><element name="TI1311709169962" sequence_nr="2" include_when_blank="false"><value><input><![CDATA[10 Pinewood]]></input></value><separator><![CDATA[CRLF]]></separator></element><element name="TI1311528790631" sequence_nr="3" include_when_blank="false"><value><input><![CDATA[Kathryn]]></input></value><separator><![CDATA[CRLF]]></separator></element><element name="MI1311864889489" sequence_nr="13" include_when_blank="false"><value><input><![CDATA[]]></input></value><separator><![CDATA[CRLF]]></separator></element><element name="BC1311866860317" sequence_nr="0" include_when_blank="true"><value><input><![CDATA[-Make a Selection-]]></input><delivery><![CDATA[nobookmark]]></delivery></value><separator><![CDATA[CRLF]]></separator></element><element name="TI1286893506835" sequence_nr="1" include_when_blank="false"><value><input><![CDATA[TI:]]></input></value><separator><![CDATA[ ]]></separator></element><element name="BC1311864384912" sequence_nr="0" include_when_blank="true"><value><input><![CDATA[Yes - immediate assistance (1)]]></input><delivery><![CDATA[BL1311864408224]]></delivery></value><separator><![CDATA[CRLF]]></separator></element><element name="TI1311528908335" sequence_nr="6" include_when_blank="false"><value><input><![CDATA[Rosetta]]></input></value><separator><![CDATA[CRLF]]></separator></element><element name="MI1311528933555" sequence_nr="7" include_when_blank="false"><value><input><![CDATA[Wants To Know Where The Parking Garage Is For The Business]]></input></value><separator><![CDATA[CRLF]]></separator></element><element name="TI1311864871224" sequence_nr="12" include_when_blank="false"><value><input><![CDATA[]]></input></value><separator><![CDATA[CRLF]]></separator></element><element name="PN1311864843131" sequence_nr="11" include_when_blank="false"><value><input><![CDATA[]]></input><input_format><![CDATA[modern]]></input_format></value><separator><![CDATA[CRLF]]></separator></element><element name="PN1311528869241" sequence_nr="5" include_when_blank="false"><value><input><![CDATA[1234562788]]></input><input_format><![CDATA[modern]]></input_format><delivery><![CDATA[1234563-2788]]></delivery></value><separator><![CDATA[CRLF]]></separator></element></element_list></custom_form_message></source_xml>
            """

    print 'target_xml %s' % target_xml
    print 'source_xml %s' % source_xml

    # Add source xml to target xml.
    try:
        # create a target DOM tree from target_xml
        s_doc = parseString(target_xml)

        # Add the source_xml to the target_doc.
        target_doc = add_xmlstr2doc(source_xml, s_doc)

        print 'combined xml %s' % target_doc.toxml()

    except ExpatError, exerr:
        print 'ExpatError: %s' % exerr

    except TypeError, tyerr:
        print 'TypeError: %s' % tyerr

