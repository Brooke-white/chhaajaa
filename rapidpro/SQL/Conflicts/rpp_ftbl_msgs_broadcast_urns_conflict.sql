DELETE FROM rappidpro.staging_rpp_ftbl_msgs_broadcast_urns
USING rappidpro.rpp_ftbl_msgs_broadcast_urns 
WHERE rpp_ftbl_msgs_broadcast_urns.id = staging_rpp_ftbl_msgs_broadcast_urns.id and rpp_ftbl_msgs_broadcast_urns.id is not null and staging_rpp_ftbl_msgs_broadcast_urns.id is not null;